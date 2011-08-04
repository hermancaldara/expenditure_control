from django.db import models


class Expense(models.Model):
    value = models.CharField(max_length=8)
    category = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s - %s - %s: %s' % (
            self.category, self.description, self.date, self.value
        )