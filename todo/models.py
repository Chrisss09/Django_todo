from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    # Creating user friendly headings
    def __str__(self):
        return self.name
