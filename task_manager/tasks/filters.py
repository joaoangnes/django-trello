import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status']

class DashboardTaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'