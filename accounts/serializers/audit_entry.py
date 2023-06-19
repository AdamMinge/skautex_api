# Third-Party import
from rest_framework import serializers
# local import
from accounts.models.audit_entry import AuditEntry


class AuditEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuditEntry
        fields = ['url', 'ip', 'logged_date', 'user']
        extra_kwargs = {
            'url': {'view_name': 'audit_entry-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['ip', 'logged_date', 'user']
