# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from accounts.views import UserContactDetailViewSet
from accounts.urls.user import user_router

user_contact_detail_router = NestedSimpleRouter(user_router, 'users', lookup='user')
user_contact_detail_router.register('contact_details', UserContactDetailViewSet, basename='user_contact_detail')

urlpatterns = [
    path('', include(user_contact_detail_router.urls)),
]
