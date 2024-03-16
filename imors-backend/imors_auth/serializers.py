from rest_framework.serializers import ModelSerializer

from imors_auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
