from django.db import transaction
from pokemons.core.logic import GenericLogic
from pokemons.exceptions import StandardException

from pokemon.dao.pokemon import PokemonDAO
from pokemon.logic.pokemon_stat import PokemonStatLogic
from pokemon.logic.stat import StatLogic
from pokemon.serializers import PokemonSerializer


class PokemonLogic(GenericLogic):

    def __init__(self):
        self.dao = PokemonDAO()
        self.serializer = PokemonSerializer

    @transaction.atomic
    def create(self, **kwargs):
        """Create a new Pokemon"""
        pokeapi_id = kwargs.get('pokeapi_id', None)
        if pokeapi_id is not None and self.dao.find(pokeapi_id=pokeapi_id).exists():
            raise StandardException('The pokemon is already created.')

        # create pokemon
        pokemon = super().create(
            name=kwargs['name'],
            weight=kwargs['weight'],
            height=kwargs['height'],
            pokeapi_id=kwargs['id']
        )

        if 'stats' in kwargs:
            # find all stats categories
            stat_logic = StatLogic()
            stats = stat_logic.data()

            # create pokemon stats
            pokemen_stat_logic = PokemonStatLogic()
            pokemen_stat_logic.bulk_create([{
                'base_stat': s['base_stat'],
                'effort': s['base_stat'],
                'stat': stat_logic.find_stat_by_name(s['stat']['name'], stats),
                'pokemon': pokemon
            } for s in kwargs['stats']])

        return pokemon

    def find_pokemon_by_name(self, name):
        """Retrieve a pokemon details with stats and evolution info by pokemon name"""
        if not name:
            raise ValueError('name have to be defined')
        return self.dao.find_pokemon_by_name(name)
