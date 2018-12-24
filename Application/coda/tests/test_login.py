from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

class LoginTestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        user1 = User.objects.create(username='Paolo')
        user1.set_password('123456')
        user1.save()

        user2 = User.objects.create(username='Michele')
        user2.set_password('coltello165')
        user2.save()

        user3 = User.objects.create(username='Giovanni')
        user3.set_password('12domenica')
        user3.save()

    def test_login_is_true1(self):
        login = self.client.login(username='Paolo', password='123456')
        print("Method: test_login_is_true1 is true")
        self.assertTrue(login)

    def test_login_is_true2(self):
        login = self.client.login(username='Michele', password='coltello165')
        print("Method: test_login_is_true2 is true")
        self.assertTrue(login)

    def test_login_is_true3(self):
        login = self.client.login(username='Giovanni', password='12domenica')
        print("Method: test_login_is_true3 is true")
        self.assertTrue(login)
