# Generated by Django 5.0.2 on 2024-11-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wasteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phonumber',
            new_name='phoneumber',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Profile_picture',
            new_name='profile_picture',
        ),
    ]
