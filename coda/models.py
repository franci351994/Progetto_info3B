from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Paziente(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    rif = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    t_arrival = models.DateTimeField(auto_now_add=True)

    priority_code = models.ForeignKey('Priority', on_delete=models.SET_NULL, blank=True, null=True)

    priority_val = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)])

    class Meta:
        permissions = (("can_see_all", "Can see all pazienti"),("can_change_priority", "Can change priority code of all pazienti"),)

    def __str__(self):

        return self.first_name + " " +  self.last_name

    def get_absolute_url(self):

        return reverse('paziente-detail', args=[str(self.rif.id)])

class Priority(models.Model):

    val = models.IntegerField()

    color = models.CharField(max_length=15)

    description = models.TextField()

    time = models.DurationField(null=True)

    def __str__(self):

        return str(self.color) + ": " + self.description

    def get_absolute_url(self):

        return reverse('priority-detail', args=[str(self.id)])
