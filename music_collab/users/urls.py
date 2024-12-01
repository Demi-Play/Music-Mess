from django.urls import path
from .views import register, login_view, logout_view, edit_profile

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('profile/edit/', edit_profile, name='edit_profile'),
]