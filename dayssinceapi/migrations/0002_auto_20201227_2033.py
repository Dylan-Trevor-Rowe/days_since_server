# Generated by Django 3.1.3 on 2020-12-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayssinceapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='date',
            field=models.CharField(default='none', max_length=10000),
        ),
    ]