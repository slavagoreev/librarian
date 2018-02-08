from django.conf.urls import url, include
from django.views import generic
from rest_framework import serializers, status
from . import views



urlpatterns = [

    url(r'^$', generic.RedirectView.as_view(
        url='/api/', permanent=False)),

    url(r'^api/documents/(?P<document_id>[0-9]+)[/]?$', views.DocumentDetail.as_view()),
    url(r'^api/documents/$', views.DocumentsByCriteria.as_view()),
    url(r'^api/tags/(?P<tag_id>[0-9]+)[/]?', views.TagDetail.as_view()),
    url(r'^api/tags/$', views.TagByCriteria.as_view()),

    url(r'^api/users/', include('rest_auth.urls')),
    url(r'^api/users/registration/', include('rest_auth.registration.urls')),

    url(r'^api/booking/(?P<document_id>[0-9]+)[/]?$', views.Booking.as_view()),
    url(r'^api/orders/(?P<order_id>[0-9]+)[/]?$', views.OrderDetail.as_view()),
    url(r'^api/orders/$', views.Orders.as_view()),
    url(r'^api/myorders/$', views.MyOrders.as_view()),
]