from django.urls import path
from . import views
urlpatterns = [
    path('',views.sign_in,name='login'),
    path('sign_up/',views.sign_up,name='sign_up'),
]