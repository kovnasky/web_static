from django.http import HttpResponce

from django.shortcuts import render
from qa.views import test

def test(request, *args, **kwards):
    return HttpResponce('OK')
