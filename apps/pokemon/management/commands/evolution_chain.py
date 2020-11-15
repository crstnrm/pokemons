from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from pokemon.logic.evolution import EvolutionLogic
from pokemon.logic.pokemon import PokemonLogic
from pokemon.logic.pokemon_stat import PokemonStatLogic
from pokemon.logic.stat import StatLogic
from pokemons.exceptions import StandardException
from pokemons.utils import generate_request

POKEAPI_URL = 'https://pokeapi.co/api/v2'


class Command(BaseCommand):
    help = 'Create a pokemon and its evolutions by PokeApiID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    @transaction.atomic
    def handle(self, *args, **options):
        evolutions_response = generate_request('{}/evolution-chain/{}/'.format(POKEAPI_URL, options['id']))

        # find all stats categories
        stat_logic = StatLogic()
        stats = stat_logic.data()

        def build_pokemons_data(data, envolves=0):
            pokemons_data = {'pokemons': [], 'stats': [], 'evolutions': []}
            species_response = generate_request(data['species']['url'])
            if species_response:
                for variety in species_response['varieties']:
                    pokemon_response = generate_request(variety['pokemon']['url'])
                    pokeapi_id = pokemon_response.pop('id')

                    # add pokemon data
                    pokemons_data['pokemons'].append({
                        'name': pokemon_response['name'],
                        'weight': pokemon_response['weight'],
                        'height': pokemon_response['height'],
                        'pokeapi_id': pokeapi_id,
                        'evolution_chain': options['id']
                    })

                    # add pokemon stats data
                    pokemons_data['stats'].extend({
                        'base_stat': stat['base_stat'],
                        'effort': stat['effort'],
                        'stat': stat_logic.find_stat_by_name(stat['stat']['name'], stats),
                        'pokeapi_id': pokeapi_id
                    } for stat in pokemon_response['stats'])

                    # add evolution pokemon data
                    pokemons_data['evolutions'].append({
                        'order': envolves,
                        'pokemon_pokeapi_id': pokeapi_id,
                        'pokeapi_id': options['id']
                    })

            for evolution in data['evolves_to']:
                temp = build_pokemons_data(evolution, envolves + 1)
                pokemons_data['pokemons'].extend(temp['pokemons'])
                pokemons_data['stats'].extend(temp['stats'])
                pokemons_data['evolutions'].extend(temp['evolutions'])
            return pokemons_data

        pokemons_data = build_pokemons_data(evolutions_response['chain'])
        pokemon_logic = PokemonLogic()
        try:
            # create pokemons
            pokemons = pokemon_logic.bulk_create(pokemons_data['pokemons'])

            # set pokemon_id to stats
            for stat in pokemons_data['stats']:
                pokemon = next(p for p in pokemons if p.pokeapi_id == stat['pokeapi_id'])
                stat['pokemon_id'] = pokemon.id
                del stat['pokeapi_id']

            # create pokemons stats
            pokemon_stat_logic = PokemonStatLogic()
            stats = pokemon_stat_logic.bulk_create(pokemons_data['stats'])

            # create pokemons evolutions
            evolution_logic = EvolutionLogic()
            evolution_obj = None
            for evolution in reversed(pokemons_data['evolutions']):
                pokemon = next(p for p in pokemons if p.pokeapi_id == evolution['pokemon_pokeapi_id'])
                evolution['pokemon'] = pokemon.id
                evolution['evolution'] = evolution_obj.id if evolution_obj else None
                del evolution['pokemon_pokeapi_id']
                evolution_obj = evolution_logic.create(**evolution)
        except (ValueError, StandardException) as err:
            raise CommandError(err.args[0])
        else:
            self.stdout.write(self.style.SUCCESS('Successfully created Pokemon "%s"' % list(pokemons)))
