# Generated by Django 4.2.1 on 2023-06-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='Old dojo', max_length=255),
        ),
    ]
