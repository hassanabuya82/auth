from djoser.serializers import UserCreateSerializer
from .models import *


class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone']

