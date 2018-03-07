from django.conf.urls import url, include

from .documents_views import DocumentDetailByCopyID, Bestsellers, DocumentDetailByDocumentID, DocumentsByCriteria

urlpatterns = [
    url(r'^(?P<document_id>[0-9]+)[/]?$', DocumentDetailByDocumentID.as_view()),
    url(r'^bestsellers/$', Bestsellers.as_view()),
    url(r'^copy/(?P<copy_id>[0-9]+)[/]?$', DocumentDetailByCopyID.as_view()),
    url(r'^$', DocumentsByCriteria.as_view()),
]