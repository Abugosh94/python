from django.shortcuts import render, redirect
from django.contrib import messages
from login_and_regestration_app.models import *
from kickball_league_app.models import *

def teams(request):
    return redirect("/home")

def new_team(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            context={
                "logged_user": User.objects.get(id= request.session['userid']),
            }
            return render(request, "add_team.html", context)
    return redirect("/success")


def add_team(request):
    errors = Team.objects.basic_validator(request.POST)
    errors2 = Team.objects.basic_validator2(request.POST)
    if len(errors) > 0 or len(errors2) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        for key, value in errors2.items():
            messages.error(request, value)
        return redirect ('/teams/new')
    else:
        this_user = User.objects.get(id=request.session["userid"])
        new_team = Team(name = request.POST["team_name"], skill_level= int(request.POST["skill_level"]), 
                        game_day= (request.POST["game_day"][0].upper()+request.POST["game_day"][1:].lower())
        , created_by = this_user)
        new_team.save()
        return redirect('/teams')
    
def view_team(request, id):
    team = Team.objects.get(id=id)
    context={
        "logged_user": User.objects.get(id= request.session['userid']),
        "team" : team,
    }
    return render(request, 'display_team.html', context)

def add_player(request, id):
    this_team = Team.objects.get(id=id)
    errors = Player.objects.basic_validator(this_team)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f'/teams/{id}')
    else:
        new_player = Player(name = request.POST["player_name"], team = this_team)
        new_player.save()
        this_team.player_count = len(this_team.players.all())
        this_team.save()

    return redirect(f"/teams/{id}")

def edit_team(request, id):
    this_team = Team.objects.get(id=id)
    this_user = User.objects.get(id= request.session['userid'])

    if this_user != this_team.created_by:
        return redirect('/home')
    
    else:
        context={
        "logged_user": this_user,
        "team" : this_team,
    }
        return render(request, 'add_team.html', context)
    
def update_team(request, id):
    this_team = Team.objects.filter(id=id)
    this_user = User.objects.get(id= request.session['userid'])

    if this_user != this_team.first().created_by:
        return redirect('/home')
    
    else:
        errors = Team.objects.basic_validator(request.POST)
        errors2 = Team.objects.basic_validator2(request.POST)
        if len(errors) > 0 or len(errors2) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            for key, value in errors2.items():
                messages.error(request, value)
            return redirect (f'/teams/{id}')
        else:
            this_team.update(name = request.POST["team_name"], skill_level= int(request.POST["skill_level"]), 
                            game_day= (request.POST["game_day"][0].upper()+request.POST["game_day"][1:].lower()))
            context={
            "logged_user": this_user,
            "team" : this_team.first(),
    }
        return render(request, 'add_team.html', context)


def delete_team(request, id):
    this_team = Team.objects.get(id=id)
    this_user = User.objects.get(id= request.session['userid'])

    if this_user == this_team.created_by:
        this_team.delete()

    return redirect('/home')

