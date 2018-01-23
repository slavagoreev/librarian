# Generated by Django 2.0.1 on 2018-01-23 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsinno', '0011_auto_20180123_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TagOfDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsinno.Document')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsinno.Tag')),
            ],
        ),
        migrations.AlterField(
            model_name='copy',
            name='document_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsinno.Document'),
        ),
        migrations.AlterField(
            model_name='documentofauthor',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsinno.Document'),
        ),
        migrations.AlterField(
            model_name='order',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsinno.Document'),
        ),
    ]