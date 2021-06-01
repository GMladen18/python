from teams.models import Team
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teams.forms import TeamForm

# Create your views here.


@login_required(login_url='login view')
def create_team_view(request, *args, ** kwargs):
    if request.method == 'GET':

        context = {
            'form': TeamForm(),
        }
        return render(request, 'create_team.html', context)
    else:
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            name = team_form.cleaned_data['name']
            image = team_form.cleaned_data['image']
            team = Team.objects.create(
                name=name, image=image, created_by=request.user)
            team.save()
            return redirect('home view')

        context = {
            'form': team_form,
        }
        return render(request, 'create-team/', context)


@login_required(login_url='login view')
def all_teams_view(request, *args, ** kwargs):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'all_teams.html', context)
