from rest_framework import serializers

from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'birthday',
                  'gender', 'phone', 'country', 'city', 'address', 'avatar')
