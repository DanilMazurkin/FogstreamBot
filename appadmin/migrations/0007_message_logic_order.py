# Generated by Django 3.1.6 on 2021-02-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0006_auto_20210215_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='logic_order',
            field=models.IntegerField(null=True),
        ),
    ]