from django.shortcuts import render
from django.http import HttpResponse
from .models import UsersCustom

def listing(request):
    """

    """
    usr = UsersCustom.objects.all()

    context = {
        'usr':usr
    }

    return render(request, 'showuser/listing.html', context)