from django.db import models
from login_and_regestration_app.models import * 

class TeamManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print("Before Here")
        weekdays = ['Sunday','Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        print(postData['game_day'].upper())
        for day in weekdays:
            if postData['game_day'].upper() == day.upper():
                errors = {}
                return errors
            else:
                errors['day_not_valid'] = "Please enter a valid day of the week ('Sunday','Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')"
        return errors
    def basic_validator2(self, postData):
        errors = {}
        if len(postData['team_name']) < 3 :
            errors['team_name'] = "Team Name should be at least 3 characters"
        if int(postData['skill_level']) > 5 or int(postData['skill_level']) < 1:
            print("Here")
            errors['skill_level'] = "Skill level should be a number between 1 and 5"
        return errors
    

    
class PlayerManager(models.Manager):
    def basic_validator(self, this_team):
        errors = {}
        if len(this_team.players.all())>=9:
            errors['full_team'] = "The Team is Full!"
        return errors


class Team(models.Model):
    name = models.CharField(max_length=45)
    skill_level = models.IntegerField(default=1)
    game_day = models.CharField(max_length=45, default="Sunday")
    created_by = models.ForeignKey(User, related_name="teams", on_delete = models.CASCADE, default= None)
    player_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TeamManager()

class Player(models.Model):
    name = models.CharField(max_length=45)
    team = models.ForeignKey(Team, related_name="players", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlayerManager()
