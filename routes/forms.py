from django import forms
from cities.models import City


class RouteForm(forms.Form):

    from_city = forms.ModelChoiceField(
        label='From', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control js-example-basic-single', 'empty_label': 'Alik'}))
    to_city = forms.ModelChoiceField(
        label='To', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    travelling_time = forms.IntegerField(label='Travel time', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Travel Time'}))
    cities = forms.ModelMultipleChoiceField(
        label='Through cities', queryset=City.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'})
    )
