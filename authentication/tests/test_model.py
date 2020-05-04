from django.test import TestCase
from authentication.models import *


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='Alyosha',
                                        surname='Gumanoid',
                                        patronymic='Krutonovich',
                                        email='alyosha@mail.ru',
                                        phone='996557775888',
                                        address='doma',
                                        birthday='19.1.1901',
                                        job='inoplanetyanin')

    def test_str(self):
        self.assertEqual(self.user.name, 'Alyosha')
        self.assertEqual(self.user.surname, 'Gumanoid')
        self.assertEqual(self.user.patronymic, 'Krutonovich')
        self.assertEqual(self.user.email, 'alyosha@mail.ru')
        self.assertEqual(self.user.phone, '996557775888')
        self.assertEqual(self.user.address, 'doma')
        self.assertEqual(self.user.birthday, '19.1.1901')
        self.assertEqual(self.user.job, 'inoplanetyanin')
