from django.conf.urls import url

from . import documents_views

urlpatterns = [
    url(r'^(?P<document_id>[0-9]+)[/]?$', documents_views.DocumentDetailByDocumentID.as_view()),
    url(r'^bestsellers/$', documents_views.Bestsellers.as_view()),
    url(r'^copy/(?P<copy_id>[0-9]+)[/]?$', documents_views.DocumentDetailByCopyID.as_view()),
    url(r'^$', documents_views.DocumentsByCriteria.as_view()),
]