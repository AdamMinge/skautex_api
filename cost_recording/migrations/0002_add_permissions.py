# Django Import
from django.db import migrations


def add_permissions(apps, schema_editor):
    cost_recording_model = apps.get_model('cost_recording', 'CostRecording')
    permission_model = apps.get_model('auth', 'Permission')
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    cost_recording_content_type = content_type_model.objects.get_for_model(cost_recording_model)

    permission_model.objects.using(db_alias).bulk_create([
        # Cost Recording Permissions
        permission_model(codename='add_own_costrecording', name='Can add own Cost Recording',
                         content_type=cost_recording_content_type),
        permission_model(codename='view_own_costrecording', name='Can view own Cost Recording',
                         content_type=cost_recording_content_type),
        permission_model(codename='change_own_costrecording', name='Can change own Cost Recording',
                         content_type=cost_recording_content_type),
        permission_model(codename='delete_own_costrecording', name='Can delete own Cost Recording',
                         content_type=cost_recording_content_type),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('cost_recording', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_permissions),
    ]
