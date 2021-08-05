from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

from .forms import UserRegistrationForm, LoginForm





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/dashboard/{user_id}/".format(user_id=user.id))

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'login_app/login.html', {'form': form})


@login_required
def dashboard(request, user_id):
    data = Profile.objects.get(pk=user_id)

    return render(request,
                  'login_app/dash_board.html',
                  {'section': 'dashboard', "user_data":data})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return render(request,
                          'login_app/register_done.html',
                          {'new_user': "vishal"})

    else:
        user_form = UserRegistrationForm()
        return render(request,
                      'login_app/register.html',
                      {'user_form': user_form})
