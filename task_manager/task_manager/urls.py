from django.contrib import admin
from django.urls import path, include
from task_manager.views import home
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),  
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', users_views.profile, name='profile'),
    path('profile/password_reset/', users_views.password_reset_with_email, name='password_reset_with_email'),
    path('tasks/', include('tasks.urls')),
    path('', home, name='home'),
]