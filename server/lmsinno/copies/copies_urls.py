from django.conf.urls import url

from . import copies_views

urlpatterns = [
    url(r'^$', copies_views.CopyDetail.as_view()),
    url(r'^(?P<copy_id>[0-9]+)[/]?$', copies_views.CopyDetail.as_view()),
]