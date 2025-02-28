from countries_plus.models import Country
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from account.models import UserBase
from account.utils import Util


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['pk', 'iso3', 'name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = UserBase
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'date_of_birth', 'country']

    def to_representation(self, instance):
        self.fields['country'] = CountrySerializer(read_only=True)
        return super(RegisterSerializer, self).to_representation(instance)

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        # Todo email ve diğerlerini check et
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric character'
            )
        # todo country eklet
        country = attrs.get('country')

        return attrs

    def create(self, validated_data):
        return UserBase.objects.create_user(**validated_data)
        # return UserBase.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = UserBase
        fields = ['token']


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        fields = ['refresh', 'access']
        read_only_fields = ['refresh', 'access']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = TokenSerializer(read_only=True)

    class Meta:
        model = UserBase
        fields = ['email', 'password', 'username', 'tokens']
        read_only_fields = ['tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        # import pdb
        # pdb.set_trace()
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')
        # todo is_active false olunca auth olmuyor
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin.')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified. ')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }


class RequestPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=3)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = UserBase.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('Token is not valid, please request a new one.')
            user.set_password(password)
            user.save()
            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid.', 401)
