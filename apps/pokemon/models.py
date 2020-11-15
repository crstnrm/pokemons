from django.db import models


class Stat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()
    evolution_chain = models.IntegerField()
    pokeapi_id = models.IntegerField()

    # I only added this snippet for demonstrate that i know to do that,
    # but it's not really necessary :)
    stats = models.ManyToManyField(
        Stat,
        through='pokemon.PokemonStat',
        through_fields=('pokemon', 'stat'),
    )

    def __str__(self):
        return self.name


class PokemonStat(models.Model):
    base_stat = models.IntegerField()
    effort = models.IntegerField()
    stat = models.ForeignKey('pokemon.Stat', on_delete=models.CASCADE)
    pokemon = models.ForeignKey('pokemon.Pokemon', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('stat', 'pokemon')


class Evolution(models.Model):
    pokemon = models.ForeignKey('pokemon.Pokemon', on_delete=models.CASCADE)
    evolution = models.ForeignKey('self', related_name='preevolution', on_delete=models.CASCADE, null=True)
    order = models.IntegerField()
    pokeapi_id = models.IntegerField()
