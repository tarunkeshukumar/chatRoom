from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Saving and logging the user
                user = form.save()
                # Log in after successful registration
                login(request, user)  
                messages.success(request, 'Registration successful! You are now logged in.')
                return redirect('chat', recipient_username=user.username)
            except Exception as e:
                # for exceptions during registraion
                logger.error(f"Error during registration: {e}")
                messages.error(request, 'An error occurred during registration. Please try again.')
                return render(request, 'chat_app/register.html', {'form': form})
        else:
            # Logs the form errors if the form is invalid
            logger.error(f"Form errors: {form.errors}")
            messages.error(request, 'There was an error with your registration. Please check the form.')
            return render(request, 'chat_app/register.html', {'form': form})
    else:
        form = UserCreationForm()

    return render(request, 'chat_app/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # for the valid form 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # if the user found, lets it login
                login(request, user)
                logger.info(f"User {user.username} logged in successfully.")
                return redirect('chat', recipient_username=user.username)
            else:
                logger.warning(f"Authentication failed for username: {username}")
                messages.error(request, 'Invalid username or password.')
        else:
            logger.warning(f"Form errors: {form.errors}")
            messages.error(request, 'Invalid username or password.')
        # for invalid form
        return render(request, 'chat_app/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'chat_app/login.html', {'form': form})

# User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Chat View
@login_required(login_url='login')
def chat_view(request, recipient_username):
    try:
        recipient = User.objects.get(username=recipient_username)
    except User.DoesNotExist:
        raise Http404("Recipient user does not exist.")
    return render(request, 'chat_app/chat.html', {'recipient_username': recipient.username,  'current_user': request.user.username,})
