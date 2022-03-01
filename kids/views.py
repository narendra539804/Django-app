from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hi This is the Intern Project</h1>")