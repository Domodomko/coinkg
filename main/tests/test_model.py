from django.test import TestCase
from main.models import *
from authentication.models import *


class NewsModelTest(TestCase):
    def setUp(self):
        self.news = News.objects.create(title='kek',
                                        content='on keknul',
                                        views=2,
                                        image='https://i.imgur.com/NNakDVF.jpg')

    def test_str(self):
        self.assertEqual(self.news.name, 'kek')
        self.assertEqual(self.news.content, 'on keknul')
        self.assertEqual(self.news.views, '2')
        self.assertEqual(self.news.image, 'https://i.imgur.com/NNakDVF.jpg')


class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(name='krya',
                                                email='kek@gmail.com',
                                                phone='996557775888',
                                                content='ya hochu pitsi')

    def test_str(self):
        self.assertEqual(self.feedback.name, 'krya')
        self.assertEqual(self.feedback.email, 'kek@gmail.com')
        self.assertEqual(self.feedback.phone, '996557775888')
        self.assertEqual(self.feedback.content, 'ya hochu pitsi')


class CreditModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name = 'Alyosha',
                                        surname='Gumanoid',
                                        patrnymic='Krutonovich',
                                        email ='alyosha@mail.ru',
                                        phone='996557775888',
                                        address='doma',
                                        birthday='19.1.1901',
                                        job='inoplanetyanin')
        self.credit = Credit.objects.create(user =self.user,
                                            sum=2000,
                                            time='20.12.2020')

    def test_str(self):
        self.assertEqual(self.credit.user, self.user)
        self.assertEqual(self.credit.sum, 2000)
        self.assertEqual(self.credit.time, '20.12.2020')