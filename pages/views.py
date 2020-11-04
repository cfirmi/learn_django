from django.shortcuts import render
from django.http import HttpResponse

def pages_about_view(*args, **kwargs):
  return HttpResponse('<h1>ABOUR VIEW VIEW</h1>')

def pages_home_view(*args, **kwargs):
  return HttpResponse('<h1>PAGESHOME VIEW</h1>')
