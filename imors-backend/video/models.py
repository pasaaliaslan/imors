from django.db.models import CASCADE, CharField, ForeignKey, Model


class OriginalVideo(Model):
    name = CharField(max_length=100)


class GeneratedVideo(Model):
    name = CharField(max_length=100)
    original_video = ForeignKey(OriginalVideo, on_delete=CASCADE)
