from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.management import call_command


class SearchPokemonTests(APITestCase):
    def setUp(self):
        # load initial data
        call_command('loaddata', 'stats.json', verbosity=0,)
        call_command('evolution_chain', '10', verbosity=0,)

    def test_search_pokemon(self):
        url = reverse('pokemon:search-pokemon', args=['pikachu'])
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
