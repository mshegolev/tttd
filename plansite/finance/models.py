from django.db import models


class Finance(models.Model):
    title = models.CharField(max_length=120)
    money = models.PositiveIntegerField()
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
