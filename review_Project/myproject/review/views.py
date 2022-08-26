from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'review/index.html')


def ver1(request):
    return render(request, 'review/ver1.html')


def ver2(request):
    return render(request, 'review/ver2.html')