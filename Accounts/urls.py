from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('register/', register, name='Register'),
    path('logout/', logout_request, name='Logout'),
    path('profile/', profile, name='Profile'),
    path('profileEdit/', profileEdit, name='ProfileEdit'),
    path('addAvatar/', addAvatar, name='addAvatar'),
    path('inbox/', inbox, name='Inbox'),
    path('sendMessage/', sendMessage, name='sendMessage'),
]