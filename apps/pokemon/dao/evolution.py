from django.db.models import Exists, OuterRef, Case, When, Value, CharField
from pokemons.core.dao import GenericDAO

from pokemon.models import Evolution


class EvolutionDAO(GenericDAO):

    def __init__(self):
        super().__init__()

        self.model = Evolution

    def find_evolutions_by_pokemon(self, pokemon):
        subquery = self.model.objects\
            .filter(pokemon=pokemon, order__lte=OuterRef('order'))
        return self.model.objects\
            .filter(pokemon__evolution_chain=pokemon.evolution_chain)\
            .exclude(pokemon=pokemon)\
            .select_related('pokemon')\
            .annotate(is_evolution=Exists(subquery))\
            .annotate(
                evolution_type=Case(
                    When(is_evolution=True, then=Value('Evolution')),
                    default=Value('Pre-Evolution'),
                    output_field=CharField(),
                ))\
            .order_by('order')
