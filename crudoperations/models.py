# from unittest.util import _MAX_LENGTH
from django.db import models
class Mytodos(models.Model):
    task=models.CharField(max_length=50)
    def __str__(self):
        return self.task