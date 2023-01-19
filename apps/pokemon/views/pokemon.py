from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pokemon.logic.evolution import EvolutionLogic
from pokemon.logic.pokemon import PokemonLogic
from pokemon.serializers import EvolutionViewSerializer
from pokemon.models import Pokemon


class FindPokemonByNameView(APIView):
    def get(self, request, name, *args, **kwargs):
        # find pokemon
        pokemon_logic = PokemonLogic()
        try:
            pokemon = pokemon_logic.find_pokemon_by_name(name)
            if pokemon is None:
                raise Pokemon.DoesNotExist
        except Pokemon.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # find all evolutions
            evolution_logic = EvolutionLogic()
            evolutions = evolution_logic.find_evolutions_by_pokemon(pokemon)
            return Response({
                'pokemon': pokemon_logic.serialize(pokemon),
                'evolutions': EvolutionViewSerializer(evolutions, many=True).data
            })
