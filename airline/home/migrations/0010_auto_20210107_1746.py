# Generated by Django 3.1.4 on 2021-01-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_merge_20210107_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.DateField(null=True, verbose_name='departure_time'),
        ),
    ]
