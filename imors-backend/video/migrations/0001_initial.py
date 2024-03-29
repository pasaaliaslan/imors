# Generated by Django 5.0.3 on 2024-03-20 00:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OriginalAudio",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                (
                    "file_type",
                    models.CharField(
                        choices=[("pcm", "pcm"), ("wav", "wav"), ("aiff", "aiff"), ("mp3", "mp3")], max_length=5
                    ),
                ),
                (
                    "uploader",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeneratedVideo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                (
                    "original_audio",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="video.originalaudio"),
                ),
            ],
        ),
    ]
