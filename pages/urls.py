from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages_home_view, name='pages-home'),
    path('pages-about/', views.pages_about_view, name='pages-about'),
]
