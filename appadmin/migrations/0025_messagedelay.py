# Generated by Django 3.1.6 on 2021-03-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0024_tokenbot'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageDelay',
            fields=[
                ('message_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='appadmin.tokenbot')),
                ('delay', models.IntegerField()),
            ],
        ),
    ]