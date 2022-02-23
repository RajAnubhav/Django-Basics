from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.huml")

def analyze(request):
    djtext= request.GET.get('removepunc', 'off')

    #check checkbox values
    analyze = request.GET.get('removepunc', 'off')

    # check if checkox is on or off
    if analyze == 'on':
        punctuations = '''!()-[{]};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        
        params = {'purpose':'Removed Punctions', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
