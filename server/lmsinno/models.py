from django.db import models

# Type of Documents:
# 0 - Book; 1 - Journal article; 2 - AV
DOCUMENT_TYPE_CHOICES = [(i, i) for i in range(2)]

# Type of User:
# 0 - basic user; 1 - Faculty; 2 - Librarian
USER_TYPE_CHOICES = [(i, i) for i in range(2)]


class Document(models.Model):
    document_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=200)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    type = models.IntegerField(choices=DOCUMENT_TYPE_CHOICES, default=0)
    price = models.FloatField()
    is_reference = models.BooleanField(default=False)
    copies_available = models.IntegerField(default=0)


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(default=None, max_length=32)
    password_salt = models.CharField(default=None, max_length=32)
    role = models.IntegerField(default=0, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True)
