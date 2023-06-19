# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework_nested import serializers
# Local import
from reports.constants import Messages
from reports.models import ReportPermission, Report


class ReportPermissionSerializer(serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'report_id': 'report__id',
    }

    default_error_messages = {
        "cannot_create_report_permission": Messages.CANNOT_CREATE_REPORT_PERMISSION_ERROR
    }

    class Meta:
        model = ReportPermission
        fields = ['url', 'report', 'user', 'permission']
        extra_kwargs = {
            'url': {'view_name': 'report_permission-detail', 'lookup_field': 'id'},
            'report': {'view_name': 'report-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['report']

    def create(self, validated_data):
        report = Report.objects.get(id=self.context["view"].kwargs["report_id"])
        validated_data["report"] = report
        try:
            report_permission = ReportPermission.objects.create(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_report_permission")
        return report_permission
