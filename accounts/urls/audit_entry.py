# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from accounts.views import AuditEntryViewSet

router = routers.SimpleRouter()
router.register('verification_times', AuditEntryViewSet, basename='audit_entry')

urlpatterns = [
    path('', include(router.urls)),
]
