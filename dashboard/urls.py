from django.urls import path
from .views import AddVessel,VesselCount

urlpatterns = [
    path('addVessel/',AddVessel.as_view()),
    path('vesselCount/',VesselCount.as_view())
]