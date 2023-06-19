# Django Import
from django.db import migrations


def add_permissions(apps, schema_editor):
    email_device_model = apps.get_model('otp_email', 'EmailDevice')
    static_device_model = apps.get_model('otp_static', 'StaticDevice')
    totp_device_model = apps.get_model('otp_totp', 'TOTPDevice')
    permission_model = apps.get_model('auth', 'Permission')
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    email_device_content_type = content_type_model.objects.get_for_model(email_device_model)
    static_device_content_type = content_type_model.objects.get_for_model(static_device_model)
    totp_device_content_type = content_type_model.objects.get_for_model(totp_device_model)

    permission_model.objects.using(db_alias).bulk_create([
        # Email Device Permissions
        permission_model(codename='add_own_emaildevice', name='Can add own email device',
                         content_type=email_device_content_type),
        permission_model(codename='view_own_emaildevice', name='Can view own email device',
                         content_type=email_device_content_type),
        permission_model(codename='change_own_emaildevice', name='Can change own email device',
                         content_type=email_device_content_type),
        permission_model(codename='delete_own_emaildevice', name='Can delete own email device',
                         content_type=email_device_content_type),

        # Static Device Permissions
        permission_model(codename='add_own_staticdevice', name='Can add own static device',
                         content_type=static_device_content_type),
        permission_model(codename='view_own_staticdevice', name='Can view own static device',
                         content_type=static_device_content_type),
        permission_model(codename='change_own_staticdevice', name='Can change own static device',
                         content_type=static_device_content_type),
        permission_model(codename='delete_own_staticdevice', name='Can delete own static device',
                         content_type=static_device_content_type),

        # TOTP Device Permissions
        permission_model(codename='add_own_totpdevice', name='Can add own TOTP device',
                         content_type=totp_device_content_type),
        permission_model(codename='view_own_totpdevice', name='Can view own TOTP device',
                         content_type=totp_device_content_type),
        permission_model(codename='change_own_totpdevice', name='Can change own TOTP device',
                         content_type=totp_device_content_type),
        permission_model(codename='delete_own_totpdevice', name='Can delete own TOTP device',
                         content_type=totp_device_content_type)

    ])


class Migration(migrations.Migration):
    dependencies = [
        ('otp_auth', '0001_initial'),
        ('otp_email', '0004_throttling'),
        ('otp_static', '0002_throttling'),
        ('otp_totp', '0002_auto_20190420_0723'),
    ]

    operations = [
        migrations.RunPython(add_permissions),
    ]
