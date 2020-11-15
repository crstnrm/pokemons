from rest_framework import serializers

from pokemon.models import Pokemon, PokemonStat, Stat, Evolution


class PokemonSerializer(serializers.ModelSerializer):
    pokemon_stats = serializers.SerializerMethodField()

    def get_pokemon_stats(self, obj):
        return PokemonStatSerializer(obj.pokemon_stats, many=True).data

    class Meta:
        model = Pokemon
        exclude = ('stats', )


class StatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = '__all__'


class PokemonStatSerializer(serializers.ModelSerializer):
    stat = StatSerializer(read_only=True, required=False)

    class Meta:
        model = PokemonStat
        exclude = ('pokemon', )


class EvolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evolution
        fields = '__all__'


class EvolutionViewSerializer(serializers.ModelSerializer):
    evolution_type = serializers.CharField(read_only=True)
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.pokemon.name

    class Meta:
        model = Evolution
        fields = ('evolution_type', 'name', 'pokeapi_id')
