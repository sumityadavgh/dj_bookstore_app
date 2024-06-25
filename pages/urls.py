from django.urls import path

from .views import HomeViewPage

urlpatterns = [
    path('', HomeViewPage.as_view(), name='home')
]
