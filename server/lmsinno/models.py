from django.db import models

# 0 - book; 1 - journal article; 2 - AV
TYPE_CHOICES = [(i, i) for i in range(2)]


class Document(models.Model):
    document_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=200)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    price = models.FloatField()
    is_reference = models.BooleanField(default=False)
    copies_available = models.IntegerField()
