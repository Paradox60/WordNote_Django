from django.shortcuts import render

def home(request):
    return render (request, 'main_app/home.html')

def page1(request):
    return render(request, 'main_app/add_words.html')

def page2(request):
    return render(request, 'main_app/test.html')

def page3(request):
    return render(request, 'main_app/library.html')
