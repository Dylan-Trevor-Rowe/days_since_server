# Generated by Django 3.1.3 on 2020-12-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayssinceapi', '0002_auto_20201227_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='date',
            field=models.DateField(),
        ),
    ]
