# Generated by Django 5.1.6 on 2025-02-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=10)),
                ('messsage', models.TextField(max_length=250)),
            ],
        ),
    ]
