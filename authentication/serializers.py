from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from informationsite import settings

from main.models import Credit
from .models import User


class AccountSerializer(serializers.ModelSerializer):
    credits = serializers.PrimaryKeyRelatedField(many=True, queryset=Credit.objects.all())

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + ('birthday', 'job', 'email', 'credits',)

