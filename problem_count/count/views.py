from django.shortcuts import render
from django.http import HttpResponse
from problem_count.settings import STATIC_URL

# Create your views here.

def index(request):
    return render(request, 'home.html', {'STATIC_URL':STATIC_URL})
