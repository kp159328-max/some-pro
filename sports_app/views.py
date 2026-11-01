from django.shortcuts import render, redirect
from .models import Team, Player

def dashboard(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    return render(request, 'sports_app/dashboard.html', {'teams': teams, 'players': players})

def add_team(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        coach = request.POST.get('coach')
        if name and coach:
            Team.objects.create(name=name, coach=coach)
        return redirect('dashboard')
    return redirect('dashboard')

def add_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        position = request.POST.get('position')
        team_id = request.POST.get('team')
        if name and age and position and team_id:
            team = Team.objects.get(id=team_id)
            Player.objects.create(name=name, age=age, position=position, team=team)
        return redirect('dashboard')
    return redirect('dashboard')
from django.shortcuts import redirect # Yeh line upar check kar lein, honi chahiye
from .models import Team, Player

# Player ko delete karne ka brain
def delete_player(request, player_id):
    player = Player.objects.get(id=player_id) # Database se us player ko dhunda
    player.delete()                           # Use hamesha ke liye mita diya
    return redirect('dashboard')              # Wapas dashboard page par bhej diya

# Team ko delete karne ka logic
def delete_team(request, team_id):
    team = Team.objects.get(id=team_id)
    team.delete() # Isse is team ke saare players bhi automatically delete ho jayenge (CASCADE effect)
    return redirect('dashboard')
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


