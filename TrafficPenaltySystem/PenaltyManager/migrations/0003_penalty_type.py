# Generated by Django 2.1.5 on 2020-05-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PenaltyManager', '0002_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='penalty',
            name='type',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
