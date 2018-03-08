from django.conf.urls import url

from . import api_documentation

urlpatterns = [
    url(r'^docs/$', api_documentation.schema_view)
]