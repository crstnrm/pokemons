from django.db.models import Prefetch
from pokemons.core.dao import GenericDAO

from pokemon.models import Pokemon, PokemonStat


class PokemonDAO(GenericDAO):

    def __init__(self):
        self.model = Pokemon

    def find_pokemon_by_name(self, name):
        return self.model.objects\
            .filter(name=name)\
            .prefetch_related(
                Prefetch(
                    'pokemonstat_set',
                    queryset=PokemonStat.objects.all().select_related('stat'),
                    to_attr='pokemon_stats'
                ))\
            .first()
