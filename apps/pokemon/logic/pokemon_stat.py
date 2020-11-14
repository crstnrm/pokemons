from pokemon.dao.pokemon_stat import PokemonStatDAO
from pokemons.core.logic import GenericLogic


class PokemonStatLogic(GenericLogic):

    def __init__(self):
        self.dao = PokemonStatDAO()


