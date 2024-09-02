from django.urls import path
from .views import Recent_Ship_IssuesView,Anomaly_DetailView

urlpatterns = [
    path('recent-ship-issues/',Recent_Ship_IssuesView.as_view()),
    path('anomaly_detail/',Anomaly_DetailView.as_view())
]