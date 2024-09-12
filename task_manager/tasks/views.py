from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter, DashboardTaskFilter

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    task_filter = TaskFilter(request.GET, queryset=tasks)
    fields = Task.get_fields()
    filtered_tasks = task_filter.qs

    paginator = Paginator(filtered_tasks, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks/task_list.html', {
        'filter': task_filter,
        'page_obj': page_obj,
        'tasks': filtered_tasks,
        'fields': fields
    })

@login_required
def task_detail_modal(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    return render(request, 'tasks/task_detail_modal.html', {'task': task})

@login_required
def dashboard(request):
    tasks = Task.objects.all().order_by('-created_at')
    task_filter = DashboardTaskFilter(request.GET, queryset=tasks)
    fields = Task.get_fields()
    filtered_tasks = task_filter.qs
    
    friendly_names = {
        'title': 'Titulo',
        'description': 'Descrição',
        'status': 'Status',
        'assigned_to': 'Atribuída a',
        'created_by': 'Criada por',
        'created_at': 'Criada em',
        'updated_at': 'Atualizada em',
    }

    paginator = Paginator(filtered_tasks, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks/dashboard.html', {
        'filter': task_filter,
        'page_obj': page_obj,
        'tasks': filtered_tasks,
        'fields': fields,
        'friendly_names': friendly_names,
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id, assigned_to=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

