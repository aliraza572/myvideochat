from django.shortcuts import render
# from django.conf.
from django.http import HttpResponse
# Create your views here.

def test_view(request):
    return HttpResponse("TEST VIEW", status=200, reason='OK')