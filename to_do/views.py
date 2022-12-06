from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from to_do.forms import TaskCreationForm
from to_do.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    queryset = Tag.objects.all()
    template_name = "to_do/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")
    template_name = "to_do/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")
    template_name = "to_do/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do:tag-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")
    paginate_by = 4


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("to_do:task-list")
    template_name = "to_do/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do/task_confirm_delete.html"
    success_url = reverse_lazy("to_do:task-list")


def toggle_status_task(request, pk):
    task = Task.objects.filter(id=pk)
    task.update(status=True) if not Task.objects.get(id=pk).status else task.update(status=False)
    return HttpResponseRedirect(reverse_lazy("to_do:task-list"))
