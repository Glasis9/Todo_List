from django.urls import path
from to_do.views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,

    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_status_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),

    path(
        "task/append/",
        TaskCreateView.as_view(),
        name="task-append",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),

    path(
        "task/<int:pk>/toggle-assign/",
        toggle_status_task,
        name="toggle-status-task",
    ),


    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tags/append/",
        TagCreateView.as_view(),
        name="tag-append",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),

]

app_name = "to_do"
