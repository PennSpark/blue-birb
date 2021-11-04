from django.shortcuts import render

def main_view(request):
    return render(request, 'main.html' )

def splash_view(request):
    return render(request, 'splash.html' )