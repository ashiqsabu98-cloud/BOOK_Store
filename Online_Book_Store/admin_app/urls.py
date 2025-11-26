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
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    #path('Register_user',views.Register_user,name="Register_user"),
    #path('login_user',views.login_user,name="login_user"),
    #path('dashboard',views.dashboard,name="dashboard"),
    #path('logout_user',views.logout_user,name="logout_user"),

    #path('admin/', admin.site.urls),
    #path('register/', views.Register_user, name="Register_user"),
    #path('login/', views.login_user, name="login_user"),
    #path('logout/', views.logout_user, name="logout_user"),

    path('add_book/',views.add_book,name='add_book'),
    path('category_list/',views.category_list,name="category_list"),
    path('add_category/',views.add_category,name="add_category"),
    path('edit_book/<int:id>',views.edit_book,name="edit_book"),
    path('delete_book/<int:id>',views.delete_book,name="delete_book"),
    path('edit_category/<int:id>',views.edit_category,name="edit_category"),
    path('delete_category/<int:id>',views.delete_category,name="delete_category"),


    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    #path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
    
]
