from django.db import models


class Boat(models.Model):
    name = models.CharField(max_length=200)
    boatSize = models.CharField(max_length=200)
    boatCapacity = models.IntegerField()
    boatPrice = models.IntegerField()

class Booking(models.Model):
    date = models.DateTimeField()
    period = models.DurationField()
    bookingNumber = models.IntegerField()



class Payment(models.Model):
    numberOfCard = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField(max_length=20)
    Transaction = models.ForeignKey(Booking)


