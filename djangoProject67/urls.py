"""djangoProject67 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, re_path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from room.views import *
from User.views import *


router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'meeting', MeetingViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    re_path(r'test/v1/user_create', userCreate),
    re_path(r'test/v1/user_login', userLogin),
    re_path(r'test/v1/get_meeting_info_month', getMeetingInfo_month),
    re_path(r'test/v1/get_meeting_info_week', getMeetingInfo_week),
    re_path(r'^test/v1/meeting_edit', meeting_update_view),
    re_path(r'^test/v1/meeting_cancel', meeting_delete_view),
    re_path(r'^test/v1/meeting_create', create_meeting),
    re_path(r'test/v1/google_reminder_create', createReminder),
]