# Generated by Django 3.1.6 on 2021-02-11 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0004_auto_20210210_0514'),
        ('appadmin', '0003_auto_20210211_1500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnswersUsers',
            new_name='Answers_Users',
        ),
        migrations.RenameModel(
            old_name='MessageInfo',
            new_name='Message_Info',
        ),
    ]
