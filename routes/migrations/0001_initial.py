# Generated by Django 3.1.1 on 2022-01-10 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0002_auto_20220104_2014'),
        ('trains', '0002_auto_20220110_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route Name')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Travel Time')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='From City')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='To City')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='List of trains')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
                'ordering': ['travel_time'],
            },
        ),
    ]