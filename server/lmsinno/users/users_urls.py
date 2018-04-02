from django.conf.urls import url
from django.urls import include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import users_views

urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^(?P<user_id>[0-9]+)[/]?$', users_views.UserDetail.as_view()),
    url(r'^$', users_views.Users.as_view()),

    url(r'^social/', include('social_django.urls', namespace='social')),  # <- Here

    url(r'^registration/$', users_views.Registration.as_view()),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', users_views.ConfirmEmail.as_view(),
        name='account_confirm_email'),
    url(r'^registration/', include('rest_auth.registration.urls')),

    url(r'^profile/(?P<user_id>[-:\w]+)/$', users_views.MyDetail.as_view()),

    url(r'^token/', obtain_jwt_token),
    url(r'^token/refresh/', refresh_jwt_token),
    url(r'^telegram/$', users_views.MyDetail.as_view())
]