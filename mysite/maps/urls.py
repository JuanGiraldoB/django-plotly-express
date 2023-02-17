from django.urls import path
from . import views

urlpatterns = [
    # path('', views.chart, name='chart')
    path('a', views.audio, name='audio'),
    path('', views.saveFileNames, name='saveFileNames')
]
