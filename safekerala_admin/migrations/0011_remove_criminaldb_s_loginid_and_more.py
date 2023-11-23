# Generated by Django 4.2.4 on 2023-11-16 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safekerala_admin', '0010_actiondb_labourdb_station_lid_stationsdb_s_loginid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminaldb',
            name='s_loginid',
        ),
        migrations.RemoveField(
            model_name='labourdb',
            name='s_loginid',
        ),
        migrations.RemoveField(
            model_name='labourdb',
            name='station_lid',
        ),
        migrations.RemoveField(
            model_name='stationsdb',
            name='s_loginid',
        ),
        migrations.AddField(
            model_name='criminaldb',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='safekerala_admin.stationsdb'),
        ),
        migrations.AddField(
            model_name='labourdb',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='safekerala_admin.stationsdb'),
        ),
    ]