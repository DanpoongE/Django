from django.urls import path
from . import views
# from throws import views

urlpatterns = [
    path('throws/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
