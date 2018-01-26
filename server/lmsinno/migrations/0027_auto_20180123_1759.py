# Generated by Django 2.0.1 on 2018-01-23 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0026_auto_20180123_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)]),
        ),
    ]