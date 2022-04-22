from django.urls import re_path
from . import views

urlpatterns = [
    re_path('price/get-all/', views.Price_CRUD.as_view()),
    re_path('price/add/', views.Price_CRUD.as_view()),
    re_path('price/update/(?P<pk>\d)/$', views.Price_CRUD.as_view()),
    re_path('price/delete/(?P<pk>\d)/$', views.Price_CRUD.as_view()),

    re_path('destribution/add/', views.Daily_Destribution_CRUD.as_view()), 
    re_path('destribution/update/(?P<pk>\d)/$', views.Daily_Destribution_CRUD.as_view()),
    re_path('destribution/delete/(?P<pk>\d)/$', views.Daily_Destribution_CRUD.as_view()),

    re_path('get-all/', views.Items_CRUD.as_view()),
    re_path('add/', views.Items_CRUD.as_view()),
    re_path('update/(?P<pk>\d)/$', views.Items_CRUD.as_view()),
    re_path('delete/(?P<pk>\d)/$', views.Items_CRUD.as_view()),

    
]