from pokemons.core.dao import GenericDAO

from pokemon.models import Stat


class StatDAO(GenericDAO):

    def __init__(self):
        self.model = Stat
