import re
from django.shortcuts import render

# Create your views here.

def bookview(request):
    return render(request, "FIRST.html")