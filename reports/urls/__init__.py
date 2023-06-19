# Django import
from django.urls import path, include


urlpatterns = [
    path('', include('reports.urls.report_player_report')),
    path('', include('reports.urls.player_report')),
    path('', include('reports.urls.report')),
    path('', include('reports.urls.report_permission')),
    path('', include('reports.urls.report_file')),
    path('', include('reports.urls.player_report_file')),
]

__all__ = ['urlpatterns']
