from django.shortcuts import render
from hello_world.models import User

# Create your views here.
def index(request):
    dict={
    'insertme':'I have been inserted dynamically to the homepage',
    }
    return render(request, 'hello_world/index.html', context=dict)

def hello_world(request):
    dict={
    'insertme':'I have been inserted dynamically to the Hello World Page'
    }
    return render(request, 'hello_world/hello.html', context=dict)

def users(request):
    dict={
    'Users': User.objects.order_by('first_name')
    }
    return render(request, 'hello_world/users.html', context=dict)
