# Generated by Django 5.1.1 on 2024-11-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_form', '0002_remove_machine_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='complaints',
            field=models.TextField(blank=True, null=True),
        ),
    ]
