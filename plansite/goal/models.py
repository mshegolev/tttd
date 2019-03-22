from django.db import models


class Goals(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    cost = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
