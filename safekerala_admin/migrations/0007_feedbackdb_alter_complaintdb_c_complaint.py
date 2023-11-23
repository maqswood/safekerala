# Generated by Django 4.2.4 on 2023-10-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safekerala_admin', '0006_complaintdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_date', models.DateField(blank=True, null=True)),
                ('f_feedback', models.CharField(blank=True, max_length=200, null=True)),
                ('u_loginid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='complaintdb',
            name='c_complaint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
