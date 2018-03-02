from django.conf.urls import url, include
from django.views import generic
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .documents import documents_views
from .tags import tags_views
from .copies import copies_views

from . import views

urlpatterns = [

    url(r'^$', generic.RedirectView.as_view(
        url='/api/', permanent=False)),

    url(r'^api/documents/(?P<document_id>[0-9]+)[/]?$', documents_views.DocumentDetailByDocumentID.as_view()),
    url(r'^api/documents/copy/(?P<copy_id>[0-9]+)[/]?$', documents_views.DocumentDetailByCopyID.as_view()),
    url(r'^api/documents/$', documents_views.DocumentsByCriteria.as_view()),

    url(r'^api/copies/$', copies_views.CopyDetail.as_view()),
    url(r'^api/copies/(?P<copy_id>[0-9]+)[/]?$', copies_views.CopyDetail.as_view()),

    url(r'^api/tags/(?P<tag_id>[0-9]+)[/]?', tags_views.TagDetail.as_view()),
    url(r'^api/tags/$', tags_views.TagByCriteria.as_view()),

    url(r'^api/users/', include('rest_auth.urls')),
    url(r'^api/users/(?P<user_id>[0-9]+)[/]?$', views.UserDetail.as_view()),
    url(r'^api/users/$', views.Users.as_view()),
    url(r'^api/users/registration/', include('rest_auth.registration.urls')),

    url(r'^api/profile/', views.MyDetail.as_view()),

    url(r'^api/users/token/', obtain_jwt_token),
    url(r'^api/users/token/refresh/', refresh_jwt_token),

    url(r'^api/booking/(?P<document_id>[0-9]+)[/]?$', views.Booking.as_view()),
    url(r'^api/orders/(?P<order_id>[0-9]+)[/]?$', views.OrderDetail.as_view()),
    url(r'^api/orders/$', views.Orders.as_view()),
    url(r'^api/myorders/$', views.MyOrders.as_view()),
    url(r'^api/myorders/(?P<order_id>[0-9]+)[/]?$', views.MyOrders.as_view()),
    url(r'^api/docs/$', views.schema_view)
]
