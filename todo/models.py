from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='list_author', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
