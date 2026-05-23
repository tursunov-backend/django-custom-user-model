from django.urls import path

from .views import (
    TodoListCreateAPIView,
    TodoDetailAPIView,
)

urlpatterns = [
    path(
        "users/<int:user_id>/todos/",
        TodoListCreateAPIView.as_view(),
        name="todo-list-create",
    ),
    path(
        "users/<int:user_id>/todos/<int:pk>/",
        TodoDetailAPIView.as_view(),
        name="todo-detail",
    ),
]