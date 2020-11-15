from pokemons.core.logic import GenericLogic

from pokemon.dao.evolution import EvolutionDAO
from pokemon.serializers import EvolutionSerializer


class EvolutionLogic(GenericLogic):

    def __init__(self):
        super().__init__()

        self.dao = EvolutionDAO()
        self.serializer = EvolutionSerializer

    def find_evolutions_by_pokemon(self, pokemon):
        """Find all evolutions by pokemon categorized by evolutions and preevolutions"""
        if pokemon is None:
            raise ValueError('pokemon have to be a valid Pokemon instance')
        return self.dao.find_evolutions_by_pokemon(pokemon)
