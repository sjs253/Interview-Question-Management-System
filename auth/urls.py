from django.urls.conf import path
from .views import login_handler, auth, signup, logout_handler

urlpatterns = [
    path('', auth, name='auth'),
    path('/login', login_handler, name='login'),
    path('/signup', signup, name='signup'),
    path('/logout', logout_handler, name='logout')
]
