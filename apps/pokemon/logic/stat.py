from pokemons.core.logic import GenericLogic

from pokemon.dao.stat import StatDAO


class StatLogic(GenericLogic):

    def __init__(self):
        super().__init__()

        self.dao = StatDAO()

    def find_stat_by_name(self, stat_name, stats):
        """ Find a stat by name

        Parameters
        ----------
        stat_name : str
        stats: Stats list or queryset

        Returns
        -------
        Stat instance
        """
        instance = None
        for stat in stats:
            if stat.name == stat_name:
                instance = stat
                break
        else:
            # don't find anything
            raise ValueError('It seems that pokeapi have changes in their response')
        return instance
