from django.urls import path


from food.views import home_view, catalog_view, price_view

urlpatterns = [
    path('', home_view),
    path('home/', home_view),
    path('catalog/', catalog_view),
    path('price/<int:pk>/', price_view),
]
