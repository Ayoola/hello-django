from django.shortcuts import render

# Create your views here.
def index(request):
    dict={
    'insertme':'I have been inserted dynamically to the homepage',
    }
    return render(request, 'index.html', context=dict)

def hello_world(request):
    dict={
    'insertme':'I have been inserted dynamically to the Hello World Page'
    }
    return render(request, 'hello_world/hello.html', context=dict)
