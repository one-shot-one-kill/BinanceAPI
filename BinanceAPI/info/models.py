from django.db import models
from django.utils import timezone


class CoinName(models.Model):
    name = models.CharField(max_length=255)
    created_data = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_data',)

    def __str__(self):
        return self.name