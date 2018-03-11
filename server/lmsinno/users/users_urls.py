from django.conf.urls import url
from django.urls import include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import users_views

urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^(?P<user_id>[0-9]+)[/]?$', users_views.UserDetail.as_view()),
    url(r'^$', users_views.Users.as_view()),
    url(r'^social/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^profile/', users_views.MyDetail.as_view()),
    url(r'^token/', obtain_jwt_token),
    url(r'^token/refresh/', refresh_jwt_token),
]