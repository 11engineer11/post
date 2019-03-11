from django.shortcuts import render,HttpResponse

# Create your views hereself.
def homeview(request):
    return HttpResponse('<b>Hosgeldiniz</b>')
