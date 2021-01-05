# Generated by Django 3.1.4 on 2021-01-05 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='flight',
        ),
        migrations.AddField(
            model_name='ticket',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.flight'),
        ),
    ]
