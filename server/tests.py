# from lmsinno.models import Document, Order, User
# from lmsinno.serializer import OrderSerializer
# from lmsinno.serializer import DocumentSerializer

from .lmsinno.serializer import DocumentSerializer
from .lmsinno.models import Document, Order, CustomUser
from .lmsinno.serializer import OrderSerializer

user = CustomUser.objects.get(pk=1)
doc = Document.objects.get(pk=1)
order = Order(document=doc, user=user, status=0, date_accepted='12/12/1222')
ser = OrderSerializer(order)
order.date_accepted = '1999-12-12'
ser = DocumentSerializer(doc, many=True)