from django.urls import path
from .views import List_of_AlertsView,Log_of_all_sent_alertsView

urlpatterns = [
    path('list_of_alert/',List_of_AlertsView.as_view()),
    path('log_of_sent_alert/',Log_of_all_sent_alertsView.as_view())
]