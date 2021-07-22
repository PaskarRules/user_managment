from django.contrib.auth.models import User
from django.core import exceptions
from rest_framework import serializers

from user_api.models import CustomUser
from user_api.validators import password_validate, email_validate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]
        extra_kwargs = {'password': {'write_only': True, 'required': False}, 'pk': {'read_only':True},
                        'username': {'required': False}}


class CustomUserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        errors = dict()
        try:
            if password:
                password_validate(password=password)
            if email:
                email_validate(email.lower())

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(CustomUserSerializer, self).validate(data)

    class Meta:
        model = CustomUser
        fields = ["pk", "username", "password", "first_name", "last_name", "email"]
        extra_kwargs = {'password': {'required': False}, 'pk': {'read_only': True},
                        'username': {'required': False}}
