from django.conf.urls import url
from Analyzer.views import ScanView,HomeView,Tech

urlpatterns = [
    url(r'^Home', HomeView.as_view(),name='Home'),
    url(r'^Scan', ScanView.as_view(), name='Scan'),
    url(r'^Tech', Tech.as_view(), name='Tech')
]