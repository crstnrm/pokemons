from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pokemon.logic.pokemon import PokemonLogic


class FindPokemonByNameView(APIView):
    def get(self, request, name, *args, **kwargs):
        logic = PokemonLogic()
        pokemon = logic.find_pokemon_by_name(name)
        if pokemon:
            return Response(logic.serialize(pokemon))
        return Response(status=status.HTTP_204_NO_CONTENT)
