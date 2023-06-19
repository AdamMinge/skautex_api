# Django Import
from django.db import migrations


def add_permissions(apps, schema_editor):
    report_model = apps.get_model('reports', 'report')
    permission_model = apps.get_model('auth', 'Permission')
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    report_model_content_type = content_type_model.objects.get_for_model(report_model)

    permission_model.objects.using(db_alias).bulk_create([
        # Report Permissions
        permission_model(codename='view_own_report', name='Can view own report',
                         content_type=report_model_content_type),
        permission_model(codename='change_own_report', name='Can change own report',
                         content_type=report_model_content_type),
        permission_model(codename='delete_own_report', name='Can delete own report',
                         content_type=report_model_content_type),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_permissions),
    ]
