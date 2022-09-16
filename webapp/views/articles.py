from django.shortcuts import render
from ..database import Cat


def stats_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        Cat.choose_action(action)
    return render(request, 'cat_stats.html', context=Cat.stats)

