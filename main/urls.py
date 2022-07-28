"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList,TaskDetail,TaskCreate,UpdateTask,TaskDelete,Login,Register

urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='http://127.0.0.1:8000/'),name='logout'),
    path('register/',Register.as_view(),name='register'),
    path('tasks/',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task details'),
    path('create-task/',TaskCreate.as_view(),name="create-task"),
    path('update-task/<int:pk>/',UpdateTask.as_view(),name="update-task"),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
    #path('login/',Login.as_view(),name='login')
]
