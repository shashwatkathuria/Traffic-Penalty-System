# Generated by Django 2.1.5 on 2020-05-13 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PenaltyManager', '0004_penalty_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penalty',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
