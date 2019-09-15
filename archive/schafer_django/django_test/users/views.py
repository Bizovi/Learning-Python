from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """
    If it's a request of type:
        POST -> Validate, instatiate with values
        GET  -> Show and render the form
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # a dictionary
            # flash message: one time alerts to the template
            messages.success(request, "Account created for {}".format(username))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
