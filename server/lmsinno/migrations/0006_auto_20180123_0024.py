# Generated by Django 2.0.1 on 2018-01-22 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0005_auto_20180123_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentsofauthor',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='documentsofauthor',
            old_name='document_id',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='document_id',
            new_name='document',
        ),
    ]
