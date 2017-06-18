from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegistrationForm, UserLoginForm, EditProfileForm, RemoveUser
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect


# All the Account views: Login, Logout, Register, Edit profile, Delete profile

def register(request):
    # Register view
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


@login_required
def edit_profile(request):
    # Edit profile view with login required
    user = request.user
    form = EditProfileForm(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name})
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']

            user.save()
            return HttpResponseRedirect('%s' % (reverse('profile')))

    args = {"form": form}

    return render(request, 'Profile/edit_profile.html', args)


@login_required
def delete_profile(request):
    # Delete Profile view with login required
    if request.method == 'POST':
        form = RemoveUser(request.POST)

        if form.is_valid():
            request.user.delete()
            auth.logout(request)
            messages.success(request, 'You have successfully deleted your account')
            return render(request, 'index.html')
        else:
            messages.error(request, "Not able to delete account!")
    else:
        form = RemoveUser()
    arg = {'form': form}
    return render(request, 'Profile/delete_profile.html', arg)


@login_required(login_url='/login/')
def profile(request):
    # Profile view with login required
    return render(request, 'Profile/profile.html')


def login(request):
    # Login view
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    # Logout view
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')
