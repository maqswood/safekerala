# Generated by Django 4.2.4 on 2023-11-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safekerala_admin', '0003_remove_actiondb_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourdb',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]