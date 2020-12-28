from rest_framework import viewsets, status
from room.models import User, Meeting
from room.serializers import UserSerializer, MeetingSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

@csrf_exempt
def getMeetingInfo_month(request):
    # data for testing
    return JsonResponse({result:1}, safe=False)
@csrf_exempt
def getMeetingInfo_week(request):
    meeting_list = [
        {
          'location': 'room31',
          'meetings': [[], [], [], [
            {
              id: 1,
              'meeting': {
                'topic': 'science',
                'host': 'Yue',
                'start': '2020-12-16T11:10:20Z',
                'end': '2020-12-16T11:11:50Z',
                'location': 'room31',
                'attendee': [{ id: 1, 'user': 'yahzee' }, { id: 2, 'user': 'evo' }, { id: 3, 'user': 'uno' }],
              },
            },
          ], [], [
            {
              id: 1,
              'meeting': {
                'topic': 'math',
                'host': 'Jeremy Lin',
                'start': '2020-12-18T12:30:20Z',
                'end': '2020-12-18T12:30:40Z',
                'location': 'room31',
                'attendee': [{ id: 1, 'user': 'george' }, { id: 2, 'user': 'roman' }, { id: 3, 'user': 'leonardo' }],
              },
            },
          ], [
            {
              id: 1,
              'meeting': {
                'topic': 'science',
                'host': 'Daniel Lin',
                'start': '2020-12-19T12:19:12Z',
                'end': '2020-12-19T16:0:12Z',
                'location': 'room31',
                'attendee': [{ id: 1, 'user': 'daniel' }, { id: 2, 'user': 'mark' }, { id: 3, 'user': 'sam' }],
              },
            },
          ],
          ],
        },
        {
          'location': 'room70',
          'meetings': [[
            {
              id: 1,
              'meeting': {
                'topic': 'architecture',
                'host': 'hyudai',
                'start': '2020-12-13T5:20:20Z',
                'end': '2020-12-13T8:30:20Z',
                'location': 'room70',
                'attendee': [{ id: 1, 'user': 'jolin' }, { id: 2, 'user': 'olivo' }, { id: 3, 'user': 'foxtrat' }],
              },
            },
          ], [], [
            {
              id: 1,
              'meeting': {
                'topic': 'physics',
                'host': 'fandom',
                'start': '2020-12-15T25:6',
                'end': '2020-12-15T27:40',
                'location': 'room70',
                'attendee': [{ id: 1, 'user': 'rosvo' }, { id: 2, 'user': 'deli' }, { id: 3, 'user': 'alin' }],
              },
            },
            {
              id: 2,
              'meeting': {
                'topic': 'software',
                'host': 'uganda',
                'start': '2020-12-15T30:70:30Z',
                'end': '2020-12-15T40:70:30Z',
                'location': 'room70',
                'attendee': [{ id: 1, 'user': 'quantun' }, { id: 2, 'user': 'fermi' }, { id: 3, 'user': 'einstein' }],
              },
            },
          ], [], [
            {
              id: 1,
              'meeting': {
                'topic': 'engineer',
                'host': 'daniel',
                'start': '2020-12-17T20:40:20Z',
                'end': '2020-12-17T22:22:20Z',
                'location': 'room70',
                'attendee': [{ id: 1, 'user': 'quantun' }, { id: 2, 'user': 'fermi' }, { id: 3, 'user': 'einstein' }],
              },
            },
          ], [], [],
          ],
        },
      ]
    return JsonResponse(meeting_list, safe=False)

@csrf_exempt
def createReminder(request):
    return JsonResponse({'result':1}, safe=False)
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
    return JsonResponse({"result":1}, safe=False)


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
    meeting.delete()
    return JsonResponse({'result':1})
