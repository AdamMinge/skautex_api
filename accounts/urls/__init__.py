# Django import
from django.urls import path, include


urlpatterns = [
    path('', include('accounts.urls.user')),
    path('', include('accounts.urls.group')),
    path('', include('accounts.urls.permission')),
    path('', include('accounts.urls.audit_entry')),
    path('', include('accounts.urls.user_all_permission')),
    path('', include('accounts.urls.user_permission')),
    path('', include('accounts.urls.user_group')),
    path('', include('accounts.urls.user_contact_detail')),
]

__all__ = ['urlpatterns']
