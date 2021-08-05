from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login view
    path('dashboard/<user_id>/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),

    path('login/', auth_views.LoginView.as_view(template_name='login_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login_app/logout.html'), name='logout'),
]
