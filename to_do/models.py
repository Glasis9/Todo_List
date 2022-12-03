from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True
    )

    class Meta:
        ordering = ["status", "-create"]

    @staticmethod
    def get_absolute_url():
        return reverse('to_do:task-list')

    def __str__(self):
        return f"{self.content} {self.status} " \
               f"Create: {self.create}" \
               f"Tags: {self.tags}"
