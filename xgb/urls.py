from django.urls import path
from .views import PublicPredView

urlpatterns = [
    path('xgb/', PublicPredView.as_view(), name="prediction"),
]