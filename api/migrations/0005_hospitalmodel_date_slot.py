# Generated by Django 3.1.5 on 2021-03-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210328_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalmodel',
            name='date_slot',
            field=models.DateField(null=True),
        ),
    ]