from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import ProjectUser, Address


class TestUserManager(TestCase):

    def setUp(self):
        self.user = mommy.make(ProjectUser)
        mommy.make(Address, _quantity=3, user=self.user, create_by=self.user)

    # unit test for user annotation of addresses count
    def test_count_annotation(self):
        user: ProjectUser = ProjectUser.with_addresses_count_objects.last()
        self.assertEqual(3, user.num_addresses)


class TestUserListView(APITestCase):

    def setUp(self):
        self.user1 = mommy.make(ProjectUser)
        self.user2 = mommy.make(ProjectUser)
        mommy.make(Address, _quantity=3, user=self.user1, create_by=self.user1)
        mommy.make(Address, _quantity=6, user=self.user2, create_by=self.user2)
        self.url = reverse('user_list')

    def test_user_list_by_min_addresses_count_filter(self):
        response = self.client.get(self.url, {'min_address_count': 4}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['uid'], str(self.user2.uid))

    def test_user_list_by_max_addresses_count_filter(self):
        response = self.client.get(self.url, {'max_address_count': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_list_by_max_min_addresses_count_filter(self):
        response = self.client.get(self.url, {'min_address_count': 2,'max_address_count':8}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
