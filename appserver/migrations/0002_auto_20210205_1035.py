# Generated by Django 3.1.6 on 2021-02-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]