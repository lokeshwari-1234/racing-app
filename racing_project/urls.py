from django.contrib import admin
from racing_app import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('racing_app.urls')),
]

