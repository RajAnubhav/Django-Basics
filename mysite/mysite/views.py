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
    
    # to check whether checkbox is on or not
    removepunc= request.GET.get('removepunc','off')

    if removepunc=="on":
        punc= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char

        params={'purpose':'Removed Punctuations', 'analyzedText':analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse('error')
        

