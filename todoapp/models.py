from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.TextField(max_length = 100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return "This is todo object"
