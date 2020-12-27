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
    # meetings = [
    #     {
    #       location: 'room31',
    #       meetings: [[], [], [], [
    #         {
    #           id: 1,
    #           meeting: {
    #             topic: 'science',
    #             host: 'Yue',
    #             start: new Date(2020, 12, 16, 11, 10),
    #             end: new Date(2020, 12, 16, 16, 60),
    #             location: 'room31',
    #             attendee: [{ id: 1, user: 'yahzee' }, { id: 2, user: 'evo' }, { id: 3, user: 'uno' }],
    #           },
    #         },
    #       ], [], [
    #         {
    #           id: 1,
    #           meeting: {
    #             topic: 'math',
    #             host: 'Jeremy Lin',
    #             start: new Date(2020, 12, 18, 12, 30),
    #             end: new Date(2020, 12, 18, 14, 2),
    #             location: 'room31',
    #             attendee: [{ id: 1, user: 'george' }, { id: 2, user: 'roman' }, { id: 3, user: 'leonardo' }],
    #           },
    #         },
    #       ], [
    #         {
    #           id: 1,
    #           meeting: {
    #             topic: 'science',
    #             host: 'Daniel Lin',
    #             start: new Date(2020, 12, 19, 12, 19),
    #             end: new Date(2020, 12, 19, 16, 0),
    #             location: 'room31',
    #             attendee: [{ id: 1, user: 'daniel' }, { id: 2, user: 'mark' }, { id: 3, user: 'sam' }],
    #           },
    #         },
    #       ],
    #       ],
    #     },
    #     {
    #       location: 'room70',
    #       meetings: [[
    #         {
    #           id: 1,
    #           meeting: {
    #             topic: 'architecture',
    #             host: 'hyudai',
    #             start: new Date(2020, 12, 13, 5, 20),
    #             end: new Date(2020, 12, 13, 8, 30),
    #             location: 'room70',
    #             attendee: [{ id: 1, user: 'jolin' }, { id: 2, user: 'olivo' }, { id: 3, user: 'foxtrat' }],
    #           },
    #         },
    #       ], [], [
    #         {
    #           id: 1,
    #           meeting: {
    #             topic: 'physics',
    #             host: 'fandom',
    #             start: new Date(2020, 12, 15, 25, 6),
    #             end: new Date(2020, 12, 15, 27, 40),
    #             location: 'room70',
    #             attendee: [{ id: 1, user: 'rosvo' }, { id: 2, user: 'deli' }, { id: 3, user: 'alin' }],
    #           },
    #         },
    #         {
    #           id: 2,
    #           meeting: {
    #             topic: 'software',
    #             host: 'uganda',
    #             start: new Date(2020, 12, 15, 30, 70),
    #             end: new Date(2020, 12, 15, 40, 70),
    #             location: 'room70',
    #             attendee: [{ id: 1, user: 'quantun' }, { id: 2, user: 'fermi' }, { id: 3, user: 'einstein' }],
    #           },
    #         },
    #       ], [], [
    #         {
    #           id: 1,
    #           meeting: {
    #             topic: 'engineer',
    #             host: 'daniel',
    #             start: new Date(2020, 12, 17, 20, 40),
    #             end: new Date(2020, 12, 17, 22, 22),
    #             location: 'room70',
    #             attendee: [{ id: 1, user: 'quantun' }, { id: 2, user: 'fermi' }, { id: 3, user: 'einstein' }],
    #           },
    #         },
    #       ], [], [],
    #       ],
    #     },

    #   ]
    return JsonResponse({'result':1}, safe=False)
@csrf_exempt
def getMeetingInfo_week(request):
    # meetings = [
    #     {
    #       topic: 'science',
    #       host: 'Daniel Lin',
    #       start: new Date(2020, 12, 20, 15, 30),
    #       end: new Date(2020, 12, 20, 16, 0),
    #       location: 'room31',
    #       attendee: [{ id: 1, user: 'daniel' }, { id: 2, user: 'mark' }, { id: 3, user: 'sam' }],
    #     },
    #     {
    #       topic: 'math',
    #       host: 'Jeremy Lin',
    #       start: new Date(2020, 12, 18, 12, 30),
    #       end: new Date(2020, 12, 18, 14, 2),
    #       location: 'hall1',
    #       attendee: [{ id: 1, user: 'george' }, { id: 2, user: 'roman' }, { id: 3, user: 'leonardo' }],
    #     },
    #     {
    #       topic: 'science',
    #       host: 'Yue',
    #       start: new Date(2020, 12, 21, 11, 10),
    #       end: new Date(2020, 12, 21, 16, 60),
    #       location: 'room34',
    #       attendee: [{ id: 1, user: 'yahzee' }, { id: 2, user: 'evo' }, { id: 3, user: 'uno' }],
    #     },
    #     {
    #       topic: 'architecture',
    #       host: 'hyudai',
    #       start: new Date(2020, 12, 22, 5, 20),
    #       end: new Date(2020, 12, 22, 8, 30),
    #       location: 'room70',
    #       attendee: [{ id: 1, user: 'jolin' }, { id: 2, user: 'olivo' }, { id: 3, user: 'foxtrat' }],
    #     },
    #     {
    #       topic: 'physics',
    #       host: 'fandom',
    #       start: new Date(2020, 12, 15, 25, 6),
    #       end: new Date(2020, 12, 15, 27, 40),
    #       location: 'room31',
    #       attendee: [{ id: 1, user: 'rosvo' }, { id: 2, user: 'deli' }, { id: 3, user: 'alin' }],
    #     },
    #     {
    #       topic: 'engineer',
    #       host: 'daniel',
    #       start: new Date(2020, 12, 11, 20, 40),
    #       end: new Date(2020, 12, 11, 22, 22),
    #       location: 'hall1',
    #       attendee: [{ id: 1, user: 'quantun' }, { id: 2, user: 'fermi' }, { id: 3, user: 'einstein' }],
    #     },
    #     {
    #       topic: 'software',
    #       host: 'uganda',
    #       start: new Date(2020, 12, 15, 30, 70),
    #       end: new Date(2020, 12, 15, 40, 70),
    #       location: 'stub11',
    #       attendee: [{ id: 1, user: 'quantun' }, { id: 2, user: 'fermi' }, { id: 3, user: 'einstein' }],
    #     },
    #   ]
    return JsonResponse({'result':1}, safe=False)

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
