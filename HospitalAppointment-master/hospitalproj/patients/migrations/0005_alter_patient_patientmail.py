# Generated by Django 5.0.1 on 2024-02-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='PatientMail',
            field=models.EmailField(max_length=40),
        ),
    ]
