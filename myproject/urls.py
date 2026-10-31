from django.contrib import admin
from django.urls import path, include
from sports_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sports/', include('sports_app.urls')),
]
