from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'document/(?P<document_id>[0-9]+)[/]?', views.DocumentDetail.as_view()),
    url(r'document/$', views.DocumentsByCriteria.as_view()),
    url(r'tag/(?P<tag_id>[0-9]+)[/]?', views.TagDetail.as_view()),
    url(r'tag/$', views.TagAll.as_view())
]


format_suffix_patterns(urlpatterns)
