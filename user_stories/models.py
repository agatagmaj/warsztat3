from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


class Reservation(models.Model):
    date = models.DateField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        unique_together = ('room_id', 'date',)
