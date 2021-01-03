from rest_framework import viewsets, status
from room.models import User, Meeting
from room.serializers import UserSerializer, MeetingSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

@csrf_exempt
def create_meeting(request):
    topic = request.POST['topic']
    host = request.POST['host']
    start= request.POST['start']
    end = request.POST['end']
    attendee = request.POST['attendee']
    room = request.POST['room']
    meeting = Meeting(topic=topic,
                      host=host,
                      start=start,
                      end=end,
                      attendee=attendee,
                      room=room,
                      )
    meeting.save()
    return JsonResponse({"result": 1}, safe=False)


@csrf_exempt
def meeting_update_view(request):
    meeting = Meeting.objects.get(pk=request.POST['id'])
    meeting.update(topic=request.POST["topic"],
                   host=request.POST["host"],
                   start=request.POST["start"],
                   end=request.POST["end"],
                   attendee=request.POST["attendee"],
                   room=request.POST["room"]
                   )
    return Response(meeting, status=status.HTTP_200_OK)

@csrf_exempt
def meeting_delete_view(request):
    meeting = Meeting.objects.get(pk=request.POST['id'])
    attendee = meeting.attendee
    attendeelist = attendee.split(str=",")
    for i in attendeelist:
        user = User.objects.get(lastname=i)
        send_mail(
            '會議已取消',
            '您所參加的會議已取消.',
            "wd97411002@gmail.com",
            [user.mail],
            fail_silently=False,
        )
    meeting.delete()
    success = JsonResponse({"data":"取消會議成功"})

    return success
