# Generated by Django 4.2.4 on 2023-08-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StationName', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Post', models.IntegerField(blank=True, null=True)),
                ('District', models.CharField(blank=True, max_length=20, null=True)),
                ('Place', models.CharField(blank=True, max_length=20, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('Latitude', models.IntegerField(blank=True, null=True)),
                ('Longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]