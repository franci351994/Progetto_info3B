from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from coda.models import Paziente,Priority

class SchedaTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):

        Priority.objects.create(
            val = 1,
            color = 'Bianco',
            description = 'pericolo bassissimo',
        )

        Paziente.objects.create(
            first_name='Samuele',
            last_name='Locatelli',
            priority_code=Priority.objects.get(color='Bianco'),
            priority_val=Priority.objects.get(color='Bianco').val,
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/coda/scheda/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('paziente-scheda'))
        self.assertEqual(response.status_code, 302)



# Create your tests here.
