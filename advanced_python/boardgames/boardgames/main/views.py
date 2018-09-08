from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.


def home(request):
    # return HttpResponse("Hello, World")
    return render(request, "main/welcome.html", {'message':'Welcome Home'})


def crudops(request):
    # Creating an entry/ Convention for APIs
    person = Person(
        nume="mihai",
        phonenumber='0761502532',
        mail="bizovim@gmail.com",
    )

    person.save()

    # Read ALL entries
    objects = Person.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'
    for elt in objects:
        res += elt.nume + "<br>"
    # Read a specific entry:
    # person = Person.objects.get(nume="pandele")
    # res += 'Printing One entry <br>'
    # res += person.nume
    #  Delete an entry
    # res += '<br> Deleting an entry <br>'
    # person.delete()
    # person.save()

    # Update
    res += 'Updating entry<br>'
    person = Person.objects.get(nume='mihai')
    person.nume = 'mihail'
    person.save()
    return HttpResponse(res)
