from django.urls import re_path
from . import views

urlpatterns = [
    re_path('add/', views.Vacations_CRUD.as_view()),
    re_path('get/(?P<pk>\d+)/$', views.Vacations_CRUD.as_view()),
    re_path('get-in-range/(?P<pk>\d+)/(?P<show_record_by>[a-z]+)/(?P<year>\d+)/(?P<month>\d+)/$', views.Vacations_CRUD.as_view()),
    re_path('get-in-range/(?P<pk>\d+)/(?P<show_record_by>[a-z]+)/(?P<year>\d+)/$', views.Vacations_CRUD.as_view()),
    re_path('get-in-range/(?P<pk>\d+)/(?P<show_record_by>[a-z]+)/$', views.Vacations_CRUD.as_view()),
    re_path('update/(?P<pk>\d+)/$', views.Vacations_CRUD.as_view()),
    re_path('delete/(?P<pk>\d+)/$', views.Vacations_CRUD.as_view()),
]