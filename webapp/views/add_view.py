from django.shortcuts import redirect

from webapp.database import Cat


def add_view(request):
    cat_name = request.POST.get('name')
    Cat.set_start_stats(cat_name)
    return redirect('http://127.0.0.1:8000/cat_stats/')
