from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Company(models.Model):
    nit = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    tel = models.PositiveIntegerField()
    dir = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)


class Project(models.Model):
    name = models.CharField(max_length=254)
    company = models.ForeignKey(Company, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

class Person(AbstractUser):
    dni = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.EmailField(max_length=254)
    username = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey(Company, null=False, blank=False, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

class Story(models.Model):
    name = models.CharField(max_length=254)
    project = models.ForeignKey(Project, null=False, blank=False, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

class Ticket(models.Model):
    states = [
        ('A', 'Activo'),
        ('P', 'En proceso'),
        ('F', 'Finalizado')
    ]
    state = models.CharField(max_length=1, choices=states, default='A')
    text = models.TextField()
    validity = models.BooleanField(default=True)
    story = models.ForeignKey(Story, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.id, self.story)