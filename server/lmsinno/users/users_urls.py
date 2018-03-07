from django.conf.urls import url
from django.urls import include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .users_views import UserDetail, Users, MyDetail

urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^(?P<user_id>[0-9]+)[/]?$', UserDetail.as_view()),
    url(r'^$', Users.as_view()),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^profile/', MyDetail.as_view()),
    url(r'^token/', obtain_jwt_token),
    url(r'^token/refresh/', refresh_jwt_token),
]