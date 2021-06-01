from django.urls import path,include
from teams.views import create_team_view, all_teams_view

urlpatterns = [
    path('create-team/', create_team_view , name="create team view"),
    path('all-teams/', all_teams_view , name="all teams view"),
]