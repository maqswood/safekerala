# Generated by Django 4.2.4 on 2023-12-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safekerala_admin', '0010_reportdb_r_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationsdb',
            name='Latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stationsdb',
            name='Longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]