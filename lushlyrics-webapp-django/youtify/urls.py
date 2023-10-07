from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('userauth.urls')),
    path('verification/', include('verify_email.urls')),
]
