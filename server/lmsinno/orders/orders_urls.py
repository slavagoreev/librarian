from django.conf.urls import url

from . import orders_views

urlpatterns = [
    url(r'^booking/(?P<document_id>[0-9]+)[/]?$', orders_views.Booking.as_view()),
    url(r'^orders/(?P<order_id>[0-9]+)[/]?$', orders_views.OrderDetail.as_view()),
    url(r'^orders/queue/$', orders_views.OrdersQueue.as_view()),
    url(r'^orders/$', orders_views.Orders.as_view()),
    url(r'^myorders/$', orders_views.MyOrders.as_view()),
    url(r'^myorders/(?P<order_id>[0-9]+)[/]?$', orders_views.MyOrders.as_view()),
]