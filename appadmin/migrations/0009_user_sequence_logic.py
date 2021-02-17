# Generated by Django 3.1.6 on 2021-02-17 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0004_auto_20210210_0514'),
        ('appadmin', '0008_question_logic_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Sequence_Logic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appserver.usertelegram')),
                ('number_record_logic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appadmin.sequence_logic')),
            ],
        ),
    ]
