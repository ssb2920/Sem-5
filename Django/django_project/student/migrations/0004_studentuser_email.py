# Generated by Django 2.2.4 on 2019-08-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190822_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
        ),
    ]
