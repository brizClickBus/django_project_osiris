from django.urls import path
from . import views
urlpatterns = [
    path('banco/',views.cad_banco,name='cad_banco'),
    path('cartoes/',views.cad_cartoes,name='cad_cartoes'),
    path('banco/ajax-autocomplete/<str:model>/', views.ajax, name='ajax-autocomplete'),
]