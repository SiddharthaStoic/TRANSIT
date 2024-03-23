from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

    path('driversignup/', views.join1, name="driversignup"),
    path('conductorsignup/', views.join2, name="conductorsignup"),
    path('tables/', views.tables_view, name='tables'),
]