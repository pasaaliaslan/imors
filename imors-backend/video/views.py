from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseServerError,
)
from django.views import View

from video.models import OriginalAudio


class GenerateVideoView(View):
    def post(self, request: HttpRequest):
        user = request.user
        audio_file = request.FILES.get("audio", None)

        if audio_file is None:
            return HttpResponseBadRequest("Audio file is not provided.")

        try:
            OriginalAudio.upload(audio_file, user)

        except ValueError as err:
            return HttpResponseBadRequest(err)

        except Exception as e:
            return HttpResponseServerError(e)

        return HttpResponse()
