"""User views"""
#Djando
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Exceptions
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile


def update_profile(request):
    return render(request, 'users/update_profile.html')


def login_view(request):
    """Login views"""
    #import pdb; pdb.set_trace() #debug
    if request.method == 'POST':

        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html') 

def signup(request):
    """Sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password dont match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        #add a profile model 
        profile = Profile(user=user)
        profile.save()

        return redirect('login')


    return render(request, 'users/signup.html')

@login_required
def logout_view(request): 
    """logout views"""
    logout(request)
    return redirect('login')
