# Generated by Django 5.1.6 on 2025-02-11 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='fullname',
        ),
    ]
