# Generated by Django 3.1.6 on 2021-02-10 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0003_auto_20210209_0738'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserTelegram',
        ),
    ]