from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('Inicio')

def about(request):
    return HttpResponse('Historia')

def services(request):
    return HttpResponse('Servicios')

def contact(request):
    return HttpResponse('Contacto')

def store(request):
    return HttpResponse('Visitanos')

def blog(request):
    return HttpResponse('Blog')

def sample(request):
    return HttpResponse('Sample')