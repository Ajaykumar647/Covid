# Generated by Django 3.1.5 on 2021-03-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalmodel',
            name='time',
            field=models.TimeField(),
        ),
    ]
