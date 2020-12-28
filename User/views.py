from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def userCreate(request):
    # 0: success
    # 1: fail
    return JsonResponse({'result':0})

@csrf_exempt
def userLogin(request):
    return JsonResponse({'result':0})
