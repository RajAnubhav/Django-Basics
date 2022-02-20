# I have created this file - Anubhav
'''
Q1. How django works?
'''
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

'''
how does django work?
- to sabse pehle urls.py is called and it looks for the 
functions call 
- then it comes back to the file named views.py 
- then it returns all the functions value which were called
'''
# def about(request):
#     return HttpResponse("This is about the first page in django")

def index(request):
    return render(request, "index.html")

def analyze(request):
    # to get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # to analyze the text
    return HttpResponse("remove punc")

# def capsFirst(request):
#     return HttpResponse("Capitalizing the text")

# def newLineRemove(request):
#     return HttpResponse("This is the New Line Remove")

# def spaceRemover(request):
#     return HttpResponse("This is space Remover")

# def charcount(request):
#     return HttpResponse("This is space count")


# this is the simple exercise in django
'''
Name of the exercise: Personal navigator websites
Take 5 websites urls and make a website and get access of the other 5 websites
hint !  html command: <href="https://www.google.com"></a>
'''


# laying the pipline in django