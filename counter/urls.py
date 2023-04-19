from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('wordcount', include('wordcount.urls')),
    path('admin/', admin.site.urls),
]
