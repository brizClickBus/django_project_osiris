from django.urls import path
from . import views
urlpatterns = [
    path('login',views.sign_in,name='login'),
    path('subscription/',views.sign_up,name='subscription'),
    path('sign_out/',views.sign_out,name='sign_out')
]