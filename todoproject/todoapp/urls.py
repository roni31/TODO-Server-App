from django.urls import path
from . import views

urlpatterns = [

    path('',views.listTask,name="task_list"),
    path('update/<str:pk>/',views.UpdateTask,name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
]