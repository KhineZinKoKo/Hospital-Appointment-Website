# Generated by Django 5.0.7 on 2024-09-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_alter_doctor_doctormail_alter_doctor_doctorph_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='PatientPh',
            field=models.IntegerField(max_length=11),
        ),
    ]
