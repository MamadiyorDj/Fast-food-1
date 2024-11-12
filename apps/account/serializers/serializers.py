from rest_framework.serializers import ModelSerializer
from apps.account.models.users import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'