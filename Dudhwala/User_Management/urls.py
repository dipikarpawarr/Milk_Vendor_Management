from django.urls import re_path
from . import views

urlpatterns = [
    re_path('user_cr/', views.userProfile_CR.as_view()),
    re_path('user_rud/(?P<pk>\d+)/$', views.userProfile_CR.as_view()),
    re_path('staff-user/', views.Staff_User.as_view()),
]