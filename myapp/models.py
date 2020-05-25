from django.db import models


class Questions(models.Model):
    name = models.CharField(max_length=20)
    question = models.TextField(max_length=600)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
