from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

class Paziente(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    rif = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    t_arrival = models.DateTimeField(auto_now_add=True)

    priority_code = models.ForeignKey('Priority', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        permissions = (("can_see_all", "Can see all pazienti"),("can_change_priority", "Can change priority code of all pazienti"),)

    def __str__(self):

        return self.first_name + " " +  self.last_name

    def get_absolute_url(self):

        return reverse('paziente-detail', args=[str(self.id)])

class Priority(models.Model):

    val = models.IntegerField()

    description = models.TextField()

    def __str__(self):

        return str(self.val) + ": " + self.description

    def get_absolute_url(self):

        return reverse('priority-detail', args=[str(self.id)])
