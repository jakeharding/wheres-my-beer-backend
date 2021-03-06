"""
tests.py - (C) Copyright - 2018
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: SEE LICENSE.txt

Author(s) of this file:
  carolynwichers

Test user endpoints.
"""

from beers.models import Beer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


class TestBeers(APITestCase):
    """
    TestBeers is a testing file to setup and retrieve beers
    """
    fixtures = ['beers/fixtures/beers.json', 'users/fixtures/users.json']

    def setUp(self):
        """
        setUp will instantiate the beer object, get the user, and force authentication
        :return:
        """
        self.beer = Beer.objects.first()
        self.user = get_user_model().objects.first()
        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        """
        test_retreive will test to see if it is able to retreive a beer from the database
        :return:
        """
        r = self.client.get('/api/dev/beers/%s' % self.beer.uuid)
        self.assertTrue(status.is_success(r.status_code), r.status_code)
        self.assertEqual(self.beer.name, r.data.get('name'))

