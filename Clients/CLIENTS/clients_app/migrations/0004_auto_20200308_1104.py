# Generated by Django 2.2.7 on 2020-03-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_app', '0003_auto_20200308_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientfile',
            name='client',
        ),
        migrations.AddField(
            model_name='clientfile',
            name='client',
            field=models.ManyToManyField(to='clients_app.Client'),
        ),
    ]