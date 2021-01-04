# Generated by Django 3.1.4 on 2021-01-04 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnr', models.CharField(max_length=10, null=True)),
                ('departure_time', models.DateTimeField(null=True)),
                ('arrival_time', models.DateTimeField(null=True)),
                ('airport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.airport')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticketclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(max_length=500, null=True)),
                ('extra_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip', models.CharField(choices=[('o', 'oneway'), ('r', 'roundtrip')], max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('seat', models.CharField(max_length=255, null=True)),
                ('flight', models.ManyToManyField(to='home.Flight')),
                ('registereduser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.registereduser')),
                ('ticketclass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ticketclass')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(choices=[('request', 'request'), ('suggestion', 'suggestion'), ('complaint', 'complaint')], max_length=255, null=True)),
                ('text', models.TextField()),
                ('registereduser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.registereduser')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumber', models.CharField(max_length=16, null=True)),
                ('cardName', models.CharField(max_length=255, null=True)),
                ('expiration', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3, null=True)),
                ('cardHolderName', models.CharField(max_length=255, null=True)),
                ('registereduser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.registereduser')),
            ],
        ),
    ]
