# Generated by Django 3.1.6 on 2021-03-07 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0033_auto_20210307_0259'),
        ('appserver', '0010_auto_20210302_0937'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserTelegram',
        ),
    ]