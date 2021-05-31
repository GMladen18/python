from django.urls import path,include

from dispecher.views import home_view,sign_up_view, user_edit_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('my-profile/', user_edit_view ,name='edit-profile'),
    path('accounts/signup/', sign_up_view , name='sign-up'),
]
