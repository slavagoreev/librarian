from django.conf.urls import url

from . import tags_views

urlpatterns = [
    url(r'^(?P<tag_id>[0-9]+)[/]?', tags_views.TagDetail.as_view()),
    url(r'^$', tags_views.TagByCriteria.as_view()),
]