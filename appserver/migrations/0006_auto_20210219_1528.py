# Generated by Django 3.1.6 on 2021-02-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0005_auto_20210219_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertelegram',
            name='first_name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='last_name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='username',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
