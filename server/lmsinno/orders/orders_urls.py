from django.conf.urls import url

from .orders_views import Booking, OrderDetail, Orders, MyOrders

urlpatterns = [
    url(r'^booking/(?P<document_id>[0-9]+)[/]?$', Booking.as_view()),
    url(r'^orders/(?P<order_id>[0-9]+)[/]?$', OrderDetail.as_view()),
    url(r'^orders/$', Orders.as_view()),
    url(r'^myorders/$', MyOrders.as_view()),
    url(r'^myorders/(?P<order_id>[0-9]+)[/]?$', MyOrders.as_view()),
]