from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'document/(?P<document_id>[0-9]+)/$', views.DocumentDetail.as_view()),
    url(r'document/$', views.DocumentsByCriteria.as_view())
    
    url(r'authorization/$', views.Authorization.as_view()),
    url(r'registration/$', views.Registration.as_view()),
]

format_suffix_patterns(urlpatterns)
