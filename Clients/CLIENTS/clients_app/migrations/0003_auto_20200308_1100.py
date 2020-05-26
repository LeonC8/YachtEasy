# Generated by Django 2.2.7 on 2020-03-08 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients_app', '0002_client_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='files',
        ),
        migrations.CreateModel(
            name='clientFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientFile', models.FileField(null=True, upload_to='')),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clients_app.Client')),
            ],
        ),
    ]
