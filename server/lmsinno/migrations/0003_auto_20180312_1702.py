# Generated by Django 2.0.1 on 2018-03-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0002_auto_20180310_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.FloatField(choices=[(0.0, 'Basic user'), (1.1, 'Instructor'), (1.2, 'TA'), (1.3, 'Professor'), (2.0, 'Librarian')], default=0),
        ),
    ]
