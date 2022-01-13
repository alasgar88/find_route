from django.db import models
from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Route Name')
    travel_time = models.PositiveSmallIntegerField(
        verbose_name='Travel Time')
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='From City')
    to_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='To City')
    trains = models.ManyToManyField(
        'trains.Train', verbose_name='List of trains')

    def __str__(self):
        return f'Route {self.name} from city {self.from_city} to city {self.to_city}'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_time']
