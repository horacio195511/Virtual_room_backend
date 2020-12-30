from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
def userCreate(request):
    name = request.POST['name']#使用者本名
    mail = request.POST['mail']#使用者信箱
    account = request.POST['account']#使用者帳號名稱
    password = request.POST['password']#使用者密碼

    if User.objects.filter(email=mail).exists():
        return JsonResponse({'result': 'mail 已存在'}, status=status.HTTP_400_BAD_REQUEST)
    elif User.objects.filter(username=account).exists():
        return JsonResponse({'result': 'account 已存在'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = User.objects.create_user(account, mail, password)
        user.last_name = name
        user.save()
        return JsonResponse({'result': 0})


@csrf_exempt
def userLogin(request):
    account = request.POST['account']#使用者帳號名稱
    password = request.POST['password']#使用者密碼

    user = auth.authenticate(username=account, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return JsonResponse({'result': 0})
    else:
        return JsonResponse({'result': 1})

@csrf_exempt
def changePassword(request):
    account = request.POST['account']#使用者帳號名稱
    password = request.POST['password']#使用者密碼
    if User.objects.filter(username=account).exists():
        u = User.objects.get(username=account)
        u.set_password(password)
        u.save()
        return JsonResponse({'result': 0})
    else:
        return Response({'result': '無效的使用者帳號'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def createReminder(request):
    id = request.POST['id']#會議ID
    reminderTime = request.POST['reminder_time']

    return JsonResponse({'result': 0})

    account = request.POST['account']#使用者帳號名稱
    password = request.POST['password']#使用者密碼
    if User.objects.filter(username=account).exists():
        u = User.objects.get(username=account)
        u.set_password(password)
        u.save()
        return JsonResponse({'result': 0})
    else:
        return Response({'result': '無效的使用者帳號'}, status=status.HTTP_400_BAD_REQUEST)
