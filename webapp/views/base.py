from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')
