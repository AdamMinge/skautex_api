# Django Import
from django.db import migrations


def add_permissions(apps, schema_editor):
    events_model = apps.get_model('calendars', 'events')
    permission_model = apps.get_model('auth', 'Permission')
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    events_model_content_type = content_type_model.objects.get_for_model(events_model)

    permission_model.objects.using(db_alias).bulk_create([
        # Events Permissions
        permission_model(codename='add_own_events', name='Can add own booking reservations',
                         content_type=events_model_content_type),
        permission_model(codename='view_own_events', name='Can view own booking reservations',
                         content_type=events_model_content_type),
        permission_model(codename='change_own_events', name='Can change own booking reservations',
                         content_type=events_model_content_type),
        permission_model(codename='delete_own_events', name='Can delete own booking reservations',
                         content_type=events_model_content_type),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_permissions),
    ]
