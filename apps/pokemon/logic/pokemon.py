from pokemons.core.logic import GenericLogic
from pokemons.exceptions import StandardException

from pokemon.dao.pokemon import PokemonDAO
from pokemon.serializers import PokemonSerializer


class PokemonLogic(GenericLogic):

    def __init__(self):
        super().__init__()

        self.dao = PokemonDAO()
        self.serializer = PokemonSerializer

    def create(self, **kwargs):
        """Create a new Pokemon"""
        pokeapi_id = kwargs.get('pokeapi_id', None)
        if pokeapi_id is not None and self.dao.find(pokeapi_id=pokeapi_id).exists():
            raise StandardException('The pokemon is already created.')
        return super().create(**kwargs)

    def find_pokemon_by_name(self, name):
        """Retrieve a pokemon details with stats and evolution info by pokemon name"""
        if not name:
            raise ValueError('name have to be defined')
        return self.dao.find_pokemon_by_name(name)
