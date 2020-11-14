from pokemons.core.logic import GenericLogic

from pokemon.dao.stat import StatDAO


class StatLogic(GenericLogic):

    def __init__(self):
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
        stat = None
        for s in stats:
            if s.name == stat_name:
                stat = s
                break
        else:
            # don't find anything
            raise ValueError('It seems that pokeapi have changes in their response')
        return stat
