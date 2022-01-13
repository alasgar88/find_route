from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City
from django.urls import reverse


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Train Number ')
    travel_time = models.PositiveSmallIntegerField(
        verbose_name='Travel Time')
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='From City')
    to_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name='To City')

    def __str__(self):
        return f'Train {self.name} from city {self.from_city} to city {self.to_city}'

    def get_absolute_url(self):
        return reverse('trains:train_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['name']

    def clean(self):
        super().clean()
        if self.from_city == self.to_city:
            raise ValidationError("Change 'To' value")
        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Change travel time")

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)
