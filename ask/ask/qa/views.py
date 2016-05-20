from django.http import HttpResponce

from django.shortcuts import render

def test(request, *args, **kwards):
    return HttpResponce('OK')
