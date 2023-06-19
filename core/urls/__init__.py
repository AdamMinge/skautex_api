# Django import
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('docs/', include('core.urls.docs')) if getattr(settings, 'DOCS_ENABLE', False) else None,
    path('health/', include('core.urls.health')) if getattr(settings, 'HEALTH_CHECK_ENABLE', False) else None,
]

urlpatterns = [pattern for pattern in urlpatterns if pattern is not None]

__all__ = ['urlpatterns']
