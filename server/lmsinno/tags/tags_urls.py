from django.conf.urls import url

from .tags_views import  TagByCriteria, TagDetail

urlpatterns = [
    url(r'^(?P<tag_id>[0-9]+)[/]?', TagDetail.as_view()),
    url(r'^$', TagByCriteria.as_view()),
]