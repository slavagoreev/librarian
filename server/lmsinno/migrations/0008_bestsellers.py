# Generated by Django 2.0.1 on 2018-01-22 21:43

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0007_copies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bestsellers',
            fields=[
                ('bestseller_id', models.AutoField(primary_key=True, serialize=False)),
                ('background_color', models.CharField(default='#000000', max_length=7)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='lmsinno.Document')),
            ],
        ),
    ]