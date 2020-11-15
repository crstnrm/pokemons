from pokemons.core.dao import GenericDAO

from pokemon.models import PokemonStat


class PokemonStatDAO(GenericDAO):

    def __init__(self):
        super().__init__()

        self.model = PokemonStat
