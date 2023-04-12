from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('create', views.TaskCreate.as_view(), name='create'),
    path('<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>', views.TaskDelete.as_view(), name='task-delete'),
]
