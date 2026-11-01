from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-team/', views.add_team, name='add_team'),
    path('add-player/', views.add_player, name='add_player'),
    path('delete-player/<int:player_id>/', views.delete_player, name='delete_player'),
    
    # BASS YEH LINE MISSING THI, ISE ADD KARNA HAI:
    path('delete-team/<int:team_id>/', views.delete_team, name='delete_team'),
]

