from django.core.files.uploadedfile import TemporaryUploadedFile
from django.db.models import CASCADE, CharField, ForeignKey, Model
from django.db.transaction import atomic

from imors_auth.models import User
from util import file_management


class OriginalAudio(Model):
    name = CharField(max_length=100)
    """Name of the original audio file uploaded by the user."""

    file_type = CharField(max_length=5, choices=[(extension, extension) for extension in ("pcm", "wav", "aiff", "mp3")])
    """File extension of the original audio file."""

    uploader = ForeignKey(User, on_delete=CASCADE)
    """Uploader for the original audio."""

    @property
    def file_path(self):
        """Path to the original audio file in the filesystem."""

        return f"video/original_audio/{self.uploader.id}/{self.id}.{self.file_type}"

    @classmethod
    def upload(self, file: TemporaryUploadedFile, uploader: User) -> None:
        """Creates a record for the audio file in db and uploads the file to the file system."""

        if uploader is None or uploader.is_anonymous:
            raise ValueError("Cannot upload a file for unauthenticated user")

        name, file_type = file.name.split(".")

        with atomic():
            # Create a record in db (metadata)
            new_original_audio_record = self.objects.create(name=name, file_type=file_type, uploader=uploader)

            # Upload the file to the file system
            file_management.upload(file=file, filepath=new_original_audio_record.file_path)


class GeneratedVideo(Model):
    name = CharField(max_length=100)
    original_audio = ForeignKey(OriginalAudio, on_delete=CASCADE)

    @property
    def file_path(self):
        """Path to the generated video file in the filesystem."""

        return f"video/generated_video/{self.original_audio.uploader.id}/{self.id}.mp4"

    def generate(self):
        raise NotImplementedError()

    def download(self):
        raise NotImplementedError()
