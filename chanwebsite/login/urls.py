from django.urls import path
from login import views
urlpatterns=[
    path('signin', views.signin),
    path('signout', views.signout),
    path('signreg', views.signreg),
]