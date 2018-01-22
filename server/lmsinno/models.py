from django.db import models


class Document(models.Model):
    # Type of Documents:
    # 0 - Book; 1 - Journal article; 2 - AV
    DOCUMENT_TYPE_CHOICES = [(i, i) for i in range(2)]

    document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, default=None)
    publisher = models.CharField(max_length=255, default=None)
    year = models.DateField()                                 # TODO read about max_length
    type = models.IntegerField(choices=DOCUMENT_TYPE_CHOICES, default=0)
    price = models.FloatField()
    is_reference = models.BooleanField(default=False)
    copies_available = models.IntegerField(default=0)
    # cover = models.ImageField()                             # TODO read about imageField


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
    phone = models.IntegerField(unique=True)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)


class DocumentsOfAuthor(models.Model):
    class Meta:
        db_table = 'lmsinno_documents_of_author'

    document = models.ForeignKey(Document, primary_key=True, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
