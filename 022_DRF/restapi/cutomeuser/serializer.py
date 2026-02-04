from rest_framework import serializers
from cutomeuser.models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleManager
        fields = ['id', 'name']


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomeUser.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            phone = validated_data['phone'],
            role = validated_data['role']
        )
        return user