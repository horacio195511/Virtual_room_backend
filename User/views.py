from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def userCreate(request):
    return JsonResponse({'result':1})


def userLogin(request):
    return JsonResponse({'result':1})
