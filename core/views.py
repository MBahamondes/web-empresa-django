from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def store(request):
    return render(request, 'core/store.html')

def sample(request):
    return render(request, 'core/sample.html')