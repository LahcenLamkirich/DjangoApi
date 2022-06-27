from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiTest),
    path('task-list/', views.taskList),
    path('create-task/', views.taskCreate),
    path('detail-task/<str:pk>/', views.taskById)
]
