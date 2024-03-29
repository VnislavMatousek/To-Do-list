from django.db import models
from django.contrib.auth.models import User

import markdown

class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
class Note(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def formatted_description(self):
        return markdown.markdown(self.description)