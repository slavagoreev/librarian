from django.conf.urls import url

from .copies_views import CopyDetail

urlpatterns = [
    url(r'^$', CopyDetail.as_view()),
    url(r'^(?P<copy_id>[0-9]+)[/]?$', CopyDetail.as_view()),
]