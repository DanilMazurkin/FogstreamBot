# Generated by Django 3.1.6 on 2021-02-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0004_auto_20210210_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertelegram',
            name='first_name',
            field=models.CharField(default='NULL', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='last_name',
            field=models.CharField(default='NULL', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='username',
            field=models.CharField(default='NULL', max_length=30, null=True),
        ),
    ]
