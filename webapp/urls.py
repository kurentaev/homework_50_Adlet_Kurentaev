from django.urls import path
from webapp.views.articles import stats_view
from webapp.views.base import index_view
from webapp.views.add_view import add_view

urlpatterns = [
    path("", index_view),
    path("add/", add_view),
    path("cat_stats/", stats_view)
]
