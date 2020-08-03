from django.urls import path

from .views import AirlineView


urlpatterns = [
    path('airplanes/', AirlineView.as_view(), name='airplane')
]
