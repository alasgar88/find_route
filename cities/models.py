from django.db import models
from django.urls import reverse
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="City name")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cities:city_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ['name']
