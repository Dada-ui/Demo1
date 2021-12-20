from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
    return HttpResponse("Hello World")

def hello(request):
    data = '''
    <!doctype html>
    <html>
        <head>
            <title>The King</title>
            <meta name="description" content="Our first page">
            <meta name="keywords" content="html tutorial template">
        </head>
        <body>
            Welcome To King's Page
        </body>
    </html>
    '''
    return HttpResponse(data)

def home(request):
    return render(request,"home.html")