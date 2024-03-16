from django.urls import path

from . import views

app_name = "video"

urlpatterns = [path("generate", views.GenerateVideoView.as_view())]
