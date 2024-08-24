from django.db import models

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    track_name = models.CharField(max_length=255)

    @staticmethod
    def get_tuple_of_tracks():
        tracks = Track.objects.all()
        return tuple((track.id, track.track_name) for track in tracks)

