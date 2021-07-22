from rest_framework import status
from django.test import Client
from django.urls import reverse

import json
import unittest

from user_api.models import CustomUser
from user_api.serializers import CustomUserSerializer

client = Client()
log_in = client.login(username='valuna', password='Triffo123')


class GetAllCustomUsersTest(unittest.TestCase):
    """ Test module for GET all users API """

    def setUp(self):
        CustomUser.objects.create(
            username='Casper', password='cAsper123')
        CustomUser.objects.create(
            username='Muffin', password='Nuffin123', first_name='Muffin')
        CustomUser.objects.create(
            username='Rambo', password='Rambo123', first_name='Rambo', last_name='Muffin')
        CustomUser.objects.create(
            username='Tubi', password='Tubi123', first_name='Tubi', last_name='Triffo')

    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('get_users'))
        # get data from db
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCustomUserTest(unittest.TestCase):
    """ Test module for GET single user API """

    def setUp(self):
        self.lupen = CustomUser.objects.create(
            username='Lupen', password='Lupen123')
        self.riki = CustomUser.objects.create(
            username='Riki', password='Riki123', first_name='Riki')
        self.rambo = CustomUser.objects.create(
            username='Rambo', password='Rambo123', first_name='Rambo', last_name='Muffin')
        self.alex = CustomUser.objects.create(
            username='Alex', password='Alex123', first_name='Alex', last_name='Triffo')

    def test_get_valid_single_user(self):
        response = client.get(
            reverse('get_user', kwargs={'pk': self.riki.pk}))
        users = CustomUser.objects.get(pk=self.riki.pk)
        serializer = CustomUserSerializer(users)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        response = client.get(
            reverse('get_user', kwargs={'pk': 10000000000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateCustomUserTest(unittest.TestCase):
    """ Test module for POST user API """

    def test_create_valid_single_user(self):
        data = {
            "username": "alex123",
            "password": "Luda23333a#",
            "first_name": "valuna",
            "last_name": "",
            "email": "ag1@asf.asf.ua"
        }

        request = client.post(reverse('create_user'), json.dumps(data), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        data_1 = {'username': 'Masha23', 'password': 'masf234asd'}
        response_1 = client.post(
            reverse('create_user'), json.dumps(data_1), content_type='application/json')

        data_2 = {'username': 'asfag', 'password': 'Ilasfaafs'}
        response_2 = client.post(
            reverse('create_user'), json.dumps(data_2), content_type='application/json')

        self.assertEqual(response_1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateCustomUserTest(unittest.TestCase):
    """ Test module for PUT user API """

    def test_create_valid_single_user(self):
        data = {
            "username": "valuna12",
            "password": "Val12#",
            "first_name": "TESTTEST",
        }

        request = client.put(reverse('update_user', args=[6]), json.dumps(data), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class DeleteCustomUserTest(unittest.TestCase):
    """ Test module for DELETE user API """

    def test_create_valid_single_user(self):
        request = client.delete(reverse('delete_user', args=[30]))
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

