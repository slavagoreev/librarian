# Generated by Django 2.0.1 on 2018-03-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0009_auto_20180330_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_attach',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
