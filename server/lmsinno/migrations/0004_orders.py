# Generated by Django 2.0.1 on 2018-01-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0003_auto_20180122_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('document_id', models.IntegerField(default=None)),
                ('user_id', models.IntegerField(default=None)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('date_accepted', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0)),
            ],
        ),
    ]