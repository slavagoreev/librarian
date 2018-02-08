from django.conf.urls import url, include
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework import serializers, status
from . import views
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # Session Login
    url(r'^login/$', views.get_auth_token, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^api/$', get_schema_view()),
]