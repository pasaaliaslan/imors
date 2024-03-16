from django.http import HttpResponse
from django.views import View


class GenerateVideoView(View):
    def get(self, request):
        a = 12
        print(a)
        return HttpResponse("Hello madafaka")
