from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("""
        <h1> Hi I am Mahim </h1>
        <hr>
        <p style="color:red"> heyyyyyyyy </p>
    
    """)


def mahim(request):
    peoples = [
        {'name': 'Mahim', 'age': 23},
        {'name': 'Mahim2', 'age': 15},
        {'name': 'Mahim3', 'age': 16},
        {'name': 'Mahim4', 'age': 18},
        {'name': 'Mahim5', 'age': 20}
    ]
    return render(request, "home/index.html", context={'peoples': peoples})


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")
