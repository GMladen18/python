from django.urls import path

from weather.views import index_view

urlpatterns = [
    path('', index_view),
]