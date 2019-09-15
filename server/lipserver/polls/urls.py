from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('tripupload', views.tripupload, name='tripupload'),
    path('addpoint', views.addpoint, name='addpoint'),
    path('tripform', views.tripform, name='tripform'),
    path('download', views.download, name='download'),
    path('gitpullonlythanks', views.gitpullonlythanks, name='gitpullonlythanks'),
]
