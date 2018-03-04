from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from ..orders.orders_serializers import OrderSerializer
from ..models import User, Order

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (email_address_exists,
                               get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.socialaccount.helpers import complete_social_login
    from allauth.socialaccount.models import SocialAccount
    from allauth.socialaccount.providers.base import AuthProcess
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'password',
                  'role',
                  'first_name',
                  'last_name',
                  'address',
                  'phone',
                  'username')


class UserSafeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    address = serializers.CharField(max_length=100, default='Innopolis')
    phone = serializers.DecimalField(max_digits=11, decimal_places=0)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    @staticmethod
    def validate_username(username):
        username = get_adapter().clean_username(username)
        return username

    @staticmethod
    def validate_email(email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError("A user is already registered with this e-mail address.")
        return email

    @staticmethod
    def validate_password1(password):
        return get_adapter().clean_password(password)

    @staticmethod
    def validate_phone(phone):
        existing_user = User.objects.filter(phone=phone)
        if existing_user and existing_user.exists():
            raise serializers.ValidationError("A user is already registered with this phone number.")
        return phone

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'address': self.validated_data.get('address', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'role': 0
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.set_data(self.cleaned_data)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'role',
                  'first_name',
                  'last_name',
                  'address',
                  'phone',
                  'username')


class UserDetailSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'role',
                  'first_name',
                  'last_name',
                  'address',
                  'phone',
                  'username',
                  'orders')

    @staticmethod
    def get_orders(obj):
        orders = OrderSerializer(Order.objects.filter(user=obj), many=True)
        return orders.data
