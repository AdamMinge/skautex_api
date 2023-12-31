# Generated by Django 2.1.15 on 2020-10-30 16:03

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
            name='BookingBlacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'verbose_name': 'Booking Blacklist',
                'verbose_name_plural': 'Booking Blacklist',
            },
        ),
        migrations.CreateModel(
            name='BookingObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Booking Object',
                'verbose_name_plural': 'Booking Objects',
            },
        ),
        migrations.CreateModel(
            name='BookingObjectsTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Booking Object Type',
                'verbose_name_plural': 'Booking Objects Types',
            },
        ),
        migrations.CreateModel(
            name='BookingReservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('booking_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_reservations', to='booking.BookingObjects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Booking Reservation',
                'verbose_name_plural': 'Booking Reservations',
            },
        ),
        migrations.AddField(
            model_name='bookingobjects',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_objects', to='booking.BookingObjectsTypes'),
        ),
        migrations.AddField(
            model_name='bookingblacklist',
            name='booking_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_blacklist', to='booking.BookingObjects'),
        ),
        migrations.AddField(
            model_name='bookingblacklist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_blacklist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='bookingblacklist',
            unique_together={('booking_object', 'user')},
        ),
    ]
