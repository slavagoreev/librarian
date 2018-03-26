from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.models import Token

from . import misc

import datetime
import jwt
import re

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class Document(models.Model):
    # Type of Documents:
    # 0 - Book; 1 - Journal article; 2 - AV
    DOCUMENT_TYPE_CHOICES = [(misc.BOOK_TYPE, 'Book'),
                             (misc.JOURNAL_TYPE, 'Journal article'),
                             (misc.AV_TYPE, 'AV')]

    title = models.CharField(max_length=255)
    document_id = models.AutoField(primary_key=True, verbose_name=title)
    description = models.TextField(blank=True, max_length=10000)
    publisher = models.CharField(max_length=255)
    year = models.IntegerField(default=datetime.datetime.now().year)
    type = models.IntegerField(choices=DOCUMENT_TYPE_CHOICES)
    price = models.FloatField()
    is_reference = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    copies_available = models.IntegerField(default=0)
    cover = models.CharField(default='empty', max_length=255)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def take_copy(self):

        copies = Copy.objects.filter(document=self).filter(status=misc.NOT_ORDERED_STATUS)

        if not copies:
            return None

        copy = copies.first()

        copy.status = misc.ORDERED_STATUS
        copy.save()

        self.copies_available -= 1
        self.save()

        return copy

    def return_copy(self, copy):
        if not copy:
            return
        if copy.document != self:
            return
        if copy.status == misc.NOT_ORDERED_STATUS:
            return

        copy.status = misc.NOT_ORDERED_STATUS
        copy.save()

        self.copies_available += 1
        self.save()


class User(AbstractUser):
    # Type of User:
    # 0 - basic user; 1 - Faculty; 2 - Librarian
    USER_TYPE_CHOICES = [(misc.BASIC_USER_ROLE, 'Basic user'),
                         (misc.INSTRUCTOR_ROLE, 'Instructor'),
                         (misc.TEACHER_ASSISTANT_ROLE, 'Teacher Assistant'),
                         (misc.VISITING_PROFESSOR_ROLE, 'Visiting Professor'),
                         (misc.PROFESSOR_ROLE, 'Professor'),
                         (misc.LIBRARIAN_ROLE, 'Librarian')]

    role = models.IntegerField(default=misc.BASIC_USER_ROLE, choices=USER_TYPE_CHOICES)
    address = models.CharField(max_length=100, default='innopolis')
    phone = models.DecimalField(unique=True, default=0, max_digits=11, decimal_places=0)

    def __str__(self):
        return '{0}'.format(self.username)

    def set_role(self, role):
        self.role = role

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_data(self, data):
        self.username = data.get('username') or self.username
        self.password = data.get('password1') or data.get('password') or self.password
        self.email = data.get('email') or self.email
        self.role = data.get('role') or self.role
        self.phone = data.get('phone') or self.phone
        self.address = data.get('address') or self.address
        self.last_name = data.get('last_name') or self.last_name
        self.first_name = data.get('first_name') or self.first_name

    @staticmethod
    def get_instance(request):
        if 'HTTP_HOST' in request.META:
            try:
                token = re.split(' ', request.META['HTTP_BEARER'])[1]
                payload = jwt.decode(token, settings.SECRET_KEY)
                email = payload['email']
                user_id = payload['user_id']

                user = User.objects.get(
                    email=email,
                    id=user_id
                )

            except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
                return None
            except User.DoesNotExist:
                return None
            except KeyError:
                return None
            # empty session catcher
            except jwt.DecodeError:
                return None

            return user
        else:
            return None


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class DocumentOfAuthor(models.Model):
    class Meta:
        db_table = 'lmsinno_document_of_author'

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{0}: {1}'.format(self.document, self.author)


class Copy(models.Model):
    # Type of Order Status
    # 0 - not ordered; 1 - ordered
    ORDER_STATUS_TYPE_CHOICES = [(i, i) for i in range(2)]

    copy_id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, to_field='document_id')
    status = models.IntegerField(choices=ORDER_STATUS_TYPE_CHOICES, default=0)
    place_hall_number = models.IntegerField(null=False)
    place_shelf_letter = models.CharField(max_length=1, null=False)

    def __str__(self):
        return '{0}: {1}'.format(str(self.copy_id), self.document)


class Order(models.Model):
    # Type of Status:
    # 0 - in queue; 1 - booked; 2 - overdue; 3 - closed; 4 - extended
    STATUS_TYPE_CHOICES = [(misc.IN_QUEUE_STATUS, 'In queue'),
                           (misc.BOOKED_STATUS, 'Booked'),
                           (misc.OVERDUE_STATUS, 'Overdue'),
                           (misc.CLOSED_STATUS, 'Closed'), ]

    order_id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, default=None, null=True)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_TYPE_CHOICES, default=misc.IN_QUEUE_STATUS)

    # date when order was created
    date_created = models.DateField(auto_now_add=True)
    # data when copy was attach to the order
    date_attach = models.DateField(default=None, null=True)
    # data when patron take his order
    date_accepted = models.DateField(default=None, null=True)
    # data when patron return his  order
    date_return = models.DateField(default=None, null=True)

    def __str__(self):
        return '{0}: {1}'.format(self.user, self.document)

    @staticmethod
    def overdue_and_queue_validation():
        """

        :return:
        """
        orders = Order.objects.all().exclude(status=misc.IN_QUEUE_STATUS).exclude(status=misc.CLOSED_STATUS)

        for order in orders:

            if order.date_return:
                if order.date_return < datetime.date.today():
                    order.status = misc.OVERDUE_STATUS
                    order.save()

        queue = Order.get_queue()
        for order in queue:
            order.attach_copy()

    @staticmethod
    def get_queue():
        orders_in_queue = Order.objects.filter(status=misc.IN_QUEUE_STATUS).filter(copy=None)

        # TODO priority queue for orders

        orders_in_queue = orders_in_queue.order_by('-user__role')
        orders_in_queue = orders_in_queue.reverse()[::-1]

        return orders_in_queue

    def attach_copy(self):
        """
        attach copy to the order if exist available copy
        :return:
        """
        if self.status != misc.IN_QUEUE_STATUS:
            return
        if self.copy:
            return

        copy = self.document.take_copy()

        if copy:
            self.date_attach = datetime.datetime.today()
            self.copy = copy
            self.save()
            # TODO notifications

    def accept(self):
        """
        accept order in queue if it has copy
        :return:
        """
        if self.status != misc.IN_QUEUE_STATUS:
            return
        self.attach_copy()
        if not self.copy:
            return

        self.date_accepted = datetime.date.today()
        delta = datetime.timedelta(days=1)

        # books are checked out for three weeks
        if self.user.role == misc.BASIC_USER_ROLE:
            delta = datetime.timedelta(weeks=3)

        # current best sellers, in which case the limit is two weeks
        if self.copy.document.is_bestseller:
            delta = datetime.timedelta(weeks=2)

        # checked out by a faculty member, in which case the limit is 4 weeks
        if self.user.role == (misc.LIBRARIAN_ROLE or
                              misc.VISITING_PROFESSOR_ROLE or
                              misc.TEACHER_ASSISTANT_ROLE or
                              misc.INSTRUCTOR_ROLE or
                              misc.PROFESSOR_ROLE):
            delta = datetime.timedelta(weeks=4)

        # AV materials and journals may be checked out for two weeks.
        if self.copy.document.type == (misc.JOURNAL_TYPE or misc.AV_TYPE):
            delta = datetime.timedelta(weeks=2)

        # Visiting Professor - limit is 1 week (regardless the type of the document)
        if self.user.role == misc.VISITING_PROFESSOR_ROLE:
            delta = datetime.timedelta(weeks=1)

        self.date_return = datetime.date.today() + delta

        self.status = misc.BOOKED_STATUS
        self.save()

    def close(self):
        """

        :return:
        """
        if self.status != (misc.BOOKED_STATUS or
                           misc.OVERDUE_STATUS or
                           misc.IN_QUEUE_STATUS):
            return None

        overdue_sum = 0
        if self.status == misc.OVERDUE_STATUS:
            overdue_days = (datetime.date.today() - self.date_return).days
            overdue_sum = min(overdue_days * 100, self.copy.document.price)

        # if order closed immediately copies number must no change
        if self.status != misc.IN_QUEUE_STATUS:
            self.date_return = datetime.date.today()

        self.document.return_copy(self.copy)
        self.status = misc.CLOSED_STATUS
        self.save()

        return overdue_sum

    def get_overdue_sum(self):
        pass


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class TagOfDocument(models.Model):
    class Meta:
        db_table = 'lmsinno_tag_of_document'

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}: {1}'.format(self.document, self.tag)
