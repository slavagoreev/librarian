# Generated by Django 2.0.1 on 2018-01-23 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0013_auto_20180123_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copy',
            old_name='document_id',
            new_name='document',
        ),
    ]