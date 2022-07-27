from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.


def Home(request):
    return HttpResponse('Home 1')


def Sobre(request):
    return HttpResponse('Sobre')


def Contato(request):
    return HttpResponse('Contato')
