from django.urls import path

from . import views # import views here 

urlpatterns = [
    path('piano/', views.piano, name='piano'),
    
]
