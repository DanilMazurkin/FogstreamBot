# Generated by Django 3.1.6 on 2021-03-02 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0030_answeruser_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeruser',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appadmin.message'),
        ),
    ]