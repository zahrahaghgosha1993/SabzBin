from django.test import TestCase
from model_mommy import mommy
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
