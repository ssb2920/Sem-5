# Generated by Django 2.2.4 on 2019-08-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190820_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='title',
            new_name='post',
        ),
    ]