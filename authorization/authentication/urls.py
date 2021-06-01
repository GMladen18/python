from django.urls import path,include
from authentication.views import home_view , login_view,register_view , logout_view


urlpatterns = [
    path('', home_view , name="home view"),
    path('login/', login_view , name="login view"),
    path('register/', register_view , name="register view"),
    path('logout/', logout_view , name="logout view"),
    
]