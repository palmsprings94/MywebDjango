from django.db import models

class Questions(models.Model):
    title = models.CharField(max_length=3, default=None)
    qbody = models.TextField(default=None)
    c1 = models.CharField(default=None)
    c2 = models.CharField(default=None)
    c3 = models.CharField(default=None)
    correctans = models.CharField(max_length=1, default=None)

    def __str__(self):
        return self.title

