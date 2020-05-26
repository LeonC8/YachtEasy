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
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat_name', models.CharField(max_length=200)),
                ('boat_description', models.CharField(max_length=500)),
                ('boat_price', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to='boats')),
                ('brand', models.CharField(max_length=200, null=True)),
                ('year', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='boats')),
                ('boats', models.ManyToManyField(to='boats.Boat')),
            ],
        ),
    ]
