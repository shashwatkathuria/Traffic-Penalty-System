from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Penalty(models.Model):
    RFID = models.CharField(max_length = 128)
    status = models.CharField(max_length = 64)
    amount = models.IntegerField()
    type = models.CharField(max_length = 64)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"RFID: {self.RFID}\nStatus: {self.status}\nAmount: {self.amount}\nType: {self.type}\nDate: {self.date}"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    RFID = models.CharField(unique = True, max_length = 128)

    def __str__(self):
        return f"User: {self.user} \nRFID: {self.RFID}"
