from django.conf.urls import url, include
from django.urls import path
from django.views import generic

urlpatterns = [

    url(r'^$', generic.RedirectView.as_view(
        url='/api/', permanent=False)),

    path(r'api/documents/', include('lmsinno.documents.documents_urls')),

    path(r'api/copies/', include('lmsinno.copies.copies_urls')),

    path(r'api/tags/', include('lmsinno.tags.tags_urls')),

    path(r'api/users/', include('lmsinno.users.users_urls')),

    path(r'api/', include('lmsinno.orders.orders_urls')),

    path(r'api/', include('lmsinno.api_documentation.api_documentation_urls'))
]
