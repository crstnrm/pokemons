from pokemons.exceptions import StandardException
from django.core.management.base import BaseCommand, CommandError
from pokemon.logic.pokemon import PokemonLogic
from pokemons.utils import generate_request


class Command(BaseCommand):
    help = 'Create a pokemon by PokeApiID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        response = generate_request('https://pokeapi.co/api/v2/pokemon/{}/'.format(options['id']))
        if response:
            pokemon_logic = PokemonLogic()
            try:
               pokemon = pokemon_logic.create(**response)
            except (ValueError, StandardException) as err:
                raise CommandError(err.args[0])
            else:
                self.stdout.write(self.style.SUCCESS('Successfully created Pokemon "%s"' % pokemon.name))
