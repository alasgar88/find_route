from django.contrib import admin
from .models import City


class CityAdmin(admin.ModelAdmin):
    class Meta:
        model = City
    list_display = ('id', 'name',)


admin.site.register(City, CityAdmin)
