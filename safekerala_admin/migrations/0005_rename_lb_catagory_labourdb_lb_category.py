# Generated by Django 4.2.4 on 2023-10-09 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safekerala_admin', '0004_labourdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labourdb',
            old_name='lb_catagory',
            new_name='lb_category',
        ),
    ]