from django.urls import path
from .views import *

urlpatterns = [
    path("",TaskListView.as_view(),name='task_list'),
    path("task/<int:pk>/",TaskDetailView.as_view(),name='task_detail'),
    path("task-create/",TaskCreateView.as_view(),name='task_create'),
    path("task-update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task-delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
    path("user-login/", UserLoginView.as_view(), name="user-login"),
path("user-logout/", LogoutView.as_view(next_page='user-login'), name="user-logout"),
path("user-register/", UserReigsterView.as_view(), name="user-register")
]
