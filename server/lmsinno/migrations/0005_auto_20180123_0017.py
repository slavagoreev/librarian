# Generated by Django 2.0.1 on 2018-01-22 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='document_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lmsinno.Document'),
        ),
    ]
