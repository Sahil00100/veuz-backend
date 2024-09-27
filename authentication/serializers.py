from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name','password', 'email']

    def create(self, validated_data):

        print(validated_data['name'])
        print(validated_data['password'])
        print(validated_data['email'])

        user = User.objects.create_user(
            first_name = validated_data["name"],
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user = "user"
        print("user created")
        return user
