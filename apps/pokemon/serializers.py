from rest_framework import serializers

from pokemon.models import Pokemon, PokemonStat, Stat


class PokemonSerializer(serializers.ModelSerializer):
    pokemon_stats = serializers.SerializerMethodField()

    def get_pokemon_stats(self, obj):
        return PokemonStatSerializer(obj.pokemon_stats, many=True).data

    class Meta:
        model = Pokemon
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = '__all__'


class PokemonStatSerializer(serializers.ModelSerializer):
    stat = StatSerializer(read_only=True, required=False)

    class Meta:
        model = PokemonStat
        fields = '__all__'
