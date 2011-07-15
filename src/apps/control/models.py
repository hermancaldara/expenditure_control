from django.db import models


class Expense(models.Model):
    value = models.CharField(max_length=8)
    category = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
