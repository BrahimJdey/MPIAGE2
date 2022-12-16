from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "User: "+self.username


class Booking(models.Model):
    bookedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.IntegerField()
    amount = models.FloatField()
    food = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    club = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    games = models.BooleanField(default=False)

    def __str__(self):
        return "Booking ID: "+str(self.id)
