from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

import datetime


class Document(models.Model):
    # Type of Documents:
    # 0 - Book; 1 - Journal article; 2 - AV
    DOCUMENT_TYPE_CHOICES = [(i, i) for i in range(2)]

    document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, default=None)
    publisher = models.CharField(max_length=255, default=None)
    year = models.IntegerField(
        default=None,
        validators=[MinLengthValidator(0), MaxLengthValidator(datetime.datetime.now().year)]
    )
    type = models.IntegerField(choices=DOCUMENT_TYPE_CHOICES, default=0)
    price = models.FloatField()
    is_reference = models.BooleanField(default=False)
    copies_available = models.IntegerField(default=0)


class User(models.Model):
    # Type of User:
    # 0 - basic user; 1 - Faculty; 2 - Librarian
    USER_TYPE_CHOICES = [(i, i) for i in range(2)]

    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(default=None, max_length=32)
    password_salt = models.CharField(default=None, max_length=32)
    role = models.IntegerField(default=0, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True,
                                default=0,
                                validators=[MinLengthValidator(10000000000),
                                            MaxLengthValidator(99999999999)])
    # TODO read about imageField


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)


class DocumentOfAuthor(models.Model):
    class Meta:
        db_table = 'lmsinno_document_of_author'

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


class Order(models.Model):
    # Type of Status:
    # 0 - in queue; 1 - booked; 2 - overdue; 3 - closed
    STATUS_TYPE_CHOICES = [(i, i) for i in range(4)]

    order_id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_created = models.DateTimeField(auto_now_add=True)
    date_accepted = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_TYPE_CHOICES, default=0)


class Copy(models.Model):
    # Type of Order Status
    # 0 - not ordered; 1 - ordered
    ORDER_STATUS_TYPE_CHOICES = [(i, i) for i in range(1)]

    copy_id = models.AutoField(primary_key=True)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ORDER_STATUS_TYPE_CHOICES, default=0)
    place_hall_number = models.IntegerField(default=0,
                                            validators=[MinLengthValidator(0),
                                                        MaxLengthValidator(9999)])
    place_shelf_letter = models.CharField(max_length=1, default='A')


class Bestseller(models.Model):
    bestseller_id = models.AutoField(primary_key=True)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=7, default='#000000')


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class TagOfDocument(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
