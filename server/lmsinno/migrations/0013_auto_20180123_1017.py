# Generated by Django 2.0.1 on 2018-01-23 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0012_auto_20180123_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestseller',
            old_name='document_id',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='tagofdocument',
            old_name='document_id',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='tagofdocument',
            old_name='tag_id',
            new_name='tag',
        ),
    ]