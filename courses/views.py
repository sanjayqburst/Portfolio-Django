from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.


def index(request):
    courses=Course.objects

    return render(request,'courses/index.html',{'courses':courses})