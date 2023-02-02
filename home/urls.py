from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('termos/',views.termos,name='termos'),
]