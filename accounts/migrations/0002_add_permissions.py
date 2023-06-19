# Django Import
from django.db import migrations


def add_permissions(apps, schema_editor):
    user_model = apps.get_model('auth', 'User')
    audit_entry_model = apps.get_model('accounts', 'AuditEntry')
    permission_model = apps.get_model('auth', 'Permission')
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    user_content_type = content_type_model.objects.get_for_model(user_model)
    audit_entry_content_type = content_type_model.objects.get_for_model(audit_entry_model)

    permission_model.objects.using(db_alias).bulk_create([
        # Audit Entry Permissions
        permission_model(codename='view_own_auditentry', name='Can view own Audit Entry',
                         content_type=audit_entry_content_type),

        # User Permissions
        permission_model(codename='view_own_user', name='Can view own user',
                         content_type=user_content_type),
        permission_model(codename='change_own_user', name='Can change own user',
                         content_type=user_content_type),
        permission_model(codename='delete_own_user', name='Can delete own user',
                         content_type=user_content_type),
        permission_model(codename='change_user_group', name='Can change user group',
                         content_type=user_content_type),
        permission_model(codename='change_user_permission', name='Can change user permission',
                         content_type=user_content_type)
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_permissions),
    ]
