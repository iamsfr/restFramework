# Generated by Django 4.1.2 on 2022-11-12 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_address_user_email_rename_phone_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='emailId',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='fullname',
        ),
    ]
