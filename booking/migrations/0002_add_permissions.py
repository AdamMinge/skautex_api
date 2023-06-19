# Django Import
from django.db import migrations


def add_permissions(apps, schema_editor):
    booking_reservations_model = apps.get_model('booking', 'BookingReservations')
    permission_model = apps.get_model('auth', 'Permission')
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    booking_reservations_content_type = content_type_model.objects.get_for_model(booking_reservations_model)

    permission_model.objects.using(db_alias).bulk_create([
        # Booking Reservations Permissions
        permission_model(codename='add_own_bookingreservations', name='Can add own booking reservations',
                         content_type=booking_reservations_content_type),
        permission_model(codename='view_own_bookingreservations', name='Can view own booking reservations',
                         content_type=booking_reservations_content_type),
        permission_model(codename='change_own_bookingreservations', name='Can change own booking reservations',
                         content_type=booking_reservations_content_type),
        permission_model(codename='delete_own_bookingreservations', name='Can delete own booking reservations',
                         content_type=booking_reservations_content_type),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_permissions),
    ]
