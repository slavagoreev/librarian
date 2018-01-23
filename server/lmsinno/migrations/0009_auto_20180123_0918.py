# Generated by Django 2.0.1 on 2018-01-23 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0008_bestsellers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bestseller',
            fields=[
                ('bestseller_id', models.AutoField(primary_key=True, serialize=False)),
                ('background_color', models.CharField(default='#000000', max_length=7)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsinno.Document')),
            ],
        ),
        migrations.RenameModel(
            old_name='Copies',
            new_name='Copy',
        ),
        migrations.RenameModel(
            old_name='DocumentsOfAuthor',
            new_name='DocumentOfAuthor',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RemoveField(
            model_name='bestsellers',
            name='document_id',
        ),
        migrations.AlterModelTable(
            name='documentofauthor',
            table='lmsinno_document_of_author',
        ),
        migrations.DeleteModel(
            name='Bestsellers',
        ),
    ]