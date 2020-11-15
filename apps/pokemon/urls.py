from django.urls import path

from .views import pokemon

app_name = 'pokemon'

urlpatterns = [
    path('search-pokemon/<str:name>/', pokemon.FindPokemonByNameView.as_view(), name='search-pokemon'),
]
