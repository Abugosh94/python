# Generated by Django 4.2.1 on 2023-06-15 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Name',
            new_name='name',
        ),
    ]
