from django.urls import path

from webapp.views import index, cat_stats, create_cat

urlpatterns = [
    path('', index),
    path('cat_stats/', cat_stats),
    path('create/', create_cat)
]