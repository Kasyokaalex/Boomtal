from django.db import models
from django.shortcuts import reverse

# Create your models here.
ART=(
    ('drawing', 'DRAWING'),
    ('carving', 'CARVING'),
)

class Art(models.Model):
    genre = models.CharField(max_length=23, choices=ART)
    name = models.CharField(max_length=20)
    file = models.FileField()



    def get_absolute_url(self):
        return reverse('artapp:hindex')

    def __str__(self):
        return self.name