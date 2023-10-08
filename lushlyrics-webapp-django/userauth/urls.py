from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("logout", views.SignOut, name='logout'),
    path("login", views.SignIn, name='login'),
    path("register", views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]