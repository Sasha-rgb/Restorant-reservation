from django.shortcuts import render
from pathlib import Path
from registration.models import UserProfile
from registration.forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout


def log_out(request):
    logout(request)
    return redirect(reverse('login'))


def home_page(request):
    context = dict()
    if request.user.username != 'admin-sasha':
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            context['user_profile'] = user_profile

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('login')) # login is the pathern name for page ....
            else:
                return HttpResponse("Your account is disabled.")# when user account is not active---

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'home_page.html', context={'login_error': "*Invalid login details supplied."})
    else:
        return render(request, 'home_page.html', context)


def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES['picture']
            else:
                profile.picture = 'profile_images/deffault.png'
            profile.save()
            registered = True
            return redirect(reverse('login'))
        else:
            return render(request, "reg_page.html", {'user_form': user_form, 'profile_form': profile_form, 'registerd': registered, "registration_error": "*Please enter a vaild information",},)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, "reg_page.html", {'user_form': user_form, 'profile_form': profile_form, 'registerd':registered})


