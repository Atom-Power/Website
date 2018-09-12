from django.shortcuts import render

# Create your views here.


def index(request):
    data = {"header": "Welcome Atom Power", "message": "Hello"}
    return render(request, 'index.html', context=data)
