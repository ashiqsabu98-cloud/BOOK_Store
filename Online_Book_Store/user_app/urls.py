"""
URL configuration for Online_Book_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    
    #path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
    #path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    #path('logout/', views.logout_user, name='logout_user'),
    path('session_login/',views.session_login,name="session_login"),
    path('session_dashboard/',views.session_dashboard,name="session_dashboard"),
    path('session_logout',views.session_logout,name="session_logout"),
]
