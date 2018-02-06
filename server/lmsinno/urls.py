from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'documents/(?P<document_id>[0-9]+)[/]?', views.DocumentDetail.as_view()),
    url(r'documents/$', views.DocumentsByCriteria.as_view()),
    url(r'tags/(?P<tag_id>[0-9]+)[/]?', views.TagDetail.as_view()),
    url(r'tags/$', views.TagByCriteria.as_view()),
    url(r'signin/', views.SignIn.as_view()),
    url(r'signup/', views.SignUp.as_view())
    url(r'^booking/(?P<document_id>[0-9]+)[/]?', views.Booking.as_view()),
    url(r'^orders/(?P<order_id>[0-9]+)[/]?', views.OrderDetail.as_view()),
    url(r'^orders/', views.Orders.as_view()),
    url(r'^myorders/$', views.MyOrders.as_view()),
]


format_suffix_patterns(urlpatterns)
