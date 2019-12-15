from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from .models import Profile


def account_page(request):

    context = {
        'page_title': 'ACCOUNT VIEW PAGE',

    }
    return render(request,'account/dashboard.html', context)

@login_required
def dashboard(request):

    context = {
        'page_title': 'Dashboard',

    }
    return render(request,'account/dashboard.html', context)

def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'account/dashboard.html',{})
                    #return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    context = {
        'page_title': 'Login',
        'form': form,
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    context = {
        'page_title': 'Register',
        'user_form': user_form,

    }

    return render(request, 'account/register.html', context)


def user_logout(request):
    logout(request)
    #redirect('account/login.html')
    return render(request, 'account/logout.html', {})
    # Redirect to a success page.




@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,
								 data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
									   data=request.POST,
									   files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			response = redirect('/account/')
			return response
			#render(request,'account/edit_success.html',{})
			#return HttpResponse('<div class="alert alert-info" role="alert">Profile updated successfully. <a href="/account/">Back to your profile.</a></div>')
			
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'account/edit.html', {'user_form': user_form,
												 'profile_form': profile_form})
