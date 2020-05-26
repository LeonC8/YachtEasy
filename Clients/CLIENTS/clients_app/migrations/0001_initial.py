# Generated by Django 2.2.7 on 2020-03-01 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('brand', models.CharField(max_length=200, null=True)),
                ('model', models.CharField(max_length=200, null=True)),
                ('year', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('look1', models.CharField(max_length=500, null=True)),
                ('look2', models.CharField(max_length=500, null=True)),
                ('budget', models.IntegerField(null=True)),
                ('first_contact', models.CharField(max_length=1000, null=True)),
                ('to_contact', models.DateField(null=True)),
                ('to_contact_text', models.CharField(max_length=1000, null=True)),
                ('communication', models.CharField(max_length=5000, null=True)),
                ('importance', models.IntegerField(null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
