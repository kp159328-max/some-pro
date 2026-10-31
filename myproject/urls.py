from django.contrib import admin
from django.urls import path, include
from sports_app import views  # <-- Nayi line jo add karni hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <-- Yeh aapka front page (`dashbour.html`) kholega
    path('sports/', include('sports_app.urls')),  # <-- Aapka purana code (taki baki pages bhi chalein)
]
