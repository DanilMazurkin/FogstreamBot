# Generated by Django 3.1.6 on 2021-02-17 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0009_user_sequence_logic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_sequence_logic',
            old_name='id_user',
            new_name='user',
        ),
    ]
