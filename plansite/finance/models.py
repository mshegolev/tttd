from django.db import models
from django.urls import reverse


class Finance(models.Model):
    title = models.CharField(max_length=120)
    costs = models.PositiveIntegerField()
    budget = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateTimeField()
    type = models.CharField(max_length=80)
    
    class Meta:
        verbose_name_plural = "Finance"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('finance_edit', kwargs={'pk': self.pk})
