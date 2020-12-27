from django.db import models


class User(models.Model):
    name = models.TextField()
    mail = models.TextField()
    account = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = "User"


class Meeting(models.Model):
    topic = models.TextField()
    host = models.TextField()
    start = models.TextField()
    end = models.TextField()
    room = models.TextField()
    attendee = models.TextField()

    class Meta:
        db_table = "Meeting"
