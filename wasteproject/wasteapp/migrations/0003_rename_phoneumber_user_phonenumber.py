# Generated by Django 5.0.2 on 2024-11-13 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wasteapp', '0002_rename_phonumber_user_phoneumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phoneumber',
            new_name='phonenumber',
        ),
    ]
