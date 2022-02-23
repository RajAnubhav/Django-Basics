from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    text = render('text', 'default')

    # check the checkbox
    removepunc= render.GET.get('removepunc', 'off')
    
    # to check if checkbox is ON
    if removepunc=="on":
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed =""
        for char in text:
            if char not in punc:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request, 'index.html', params)
    
    else:
        return HttpResponse("Error")