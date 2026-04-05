from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.stockPicker, name='stockpicker'),
    path('stocktracker/', views.stockTracker, name = 'stocktracker'),
]