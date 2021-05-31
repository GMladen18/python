from django.urls import path

from django_auth.views import registration_view, logout_view

urlpatterns = [
    path('registration/' , registration_view , name='registration'),
    path('logout/' , logout_view , name='logout')
]