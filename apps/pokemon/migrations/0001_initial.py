# Generated by Django 3.1.3 on 2020-11-14 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('pokeapi_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_stat', models.IntegerField()),
                ('effort', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemon')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.stat')),
            ],
            options={
                'unique_together': {('stat', 'pokemon')},
            },
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stats',
            field=models.ManyToManyField(through='pokemon.PokemonStat', to='pokemon.Stat'),
        ),
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemon')),
            ],
        ),
    ]
