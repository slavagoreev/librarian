# Generated by Django 2.0.1 on 2018-02-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0002_auto_20180206_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='innopoli', max_length=100),
        ),
    ]
