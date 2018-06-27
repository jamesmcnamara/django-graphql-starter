from django.db import models

class Ship(models.Model):
    name = models.CharField(max_length=255)

class Rebel(models.Model):
    name = models.CharField(max_length=255)
    ship = models.ForeignKey(Ship, related_name='crew', on_delete=models.CASCADE)
