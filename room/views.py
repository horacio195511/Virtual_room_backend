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
    # 初始化該月份的 meeting info (default = [])
    result = {}
    for i in range(1,32):
        tmp = []
        result[i] = tmp
    
    # 取 meeting table 的所有資料
    data = Meeting.objects.all()
    for i in range(len(data)):
        # 抓該年份以及該月份的 meeting 資料
        if(data[i].start[0:4] == request.POST['year'] and int(data[i].start[5:7]) == int(request.POST['month'])):
            # 抓日期資料
            if(data[i].start[8:10] == "01"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[1].append(tmp_dict)
            elif(data[i].start[8:10] == "02"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[2].append(tmp_dict)
            elif(data[i].start[8:10] == "03"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[3].append(tmp_dict)
            elif(data[i].start[8:10] == "04"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[4].append(tmp_dict)
            elif(data[i].start[8:10] == "05"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[5].append(tmp_dict)
            elif(data[i].start[8:10] == "06"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[6].append(tmp_dict)
            elif(data[i].start[8:10] == "07"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[7].append(tmp_dict)
            elif(data[i].start[8:10] == "08"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[8].append(tmp_dict)
            elif(data[i].start[8:10] == "09"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[9].append(tmp_dict)
            elif(data[i].start[8:10] == "10"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[10].append(tmp_dict)
            elif(data[i].start[8:10] == "11"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[11].append(tmp_dict)
            elif(data[i].start[8:10] == "12"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[12].append(tmp_dict)
            elif(data[i].start[8:10] == "13"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[13].append(tmp_dict)
            elif(data[i].start[8:10] == "14"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[14].append(tmp_dict)
            elif(data[i].start[8:10] == "15"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[15].append(tmp_dict)
            elif(data[i].start[8:10] == "16"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[16].append(tmp_dict)
            elif(data[i].start[8:10] == "17"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[17].append(tmp_dict)
            elif(data[i].start[8:10] == "18"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[18].append(tmp_dict)
            elif(data[i].start[8:10] == "19"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[19].append(tmp_dict)
            elif(data[i].start[8:10] == "20"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[20].append(tmp_dict)
            elif(data[i].start[8:10] == "21"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[21].append(tmp_dict)
            elif(data[i].start[8:10] == "22"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[22].append(tmp_dict)
            elif(data[i].start[8:10] == "23"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[23].append(tmp_dict)
            elif(data[i].start[8:10] == "24"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[24].append(tmp_dict)
            elif(data[i].start[8:10] == "25"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[25].append(tmp_dict)
            elif(data[i].start[8:10] == "26"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[26].append(tmp_dict)
            elif(data[i].start[8:10] == "27"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[27].append(tmp_dict)
            elif(data[i].start[8:10] == "28"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[28].append(tmp_dict)
            elif(data[i].start[8:10] == "29"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[29].append(tmp_dict)
            elif(data[i].start[8:10] == "30"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[30].append(tmp_dict)
            elif(data[i].start[8:10] == "31"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[31].append(tmp_dict)

    return JsonResponse(result, safe=False)

@csrf_exempt
def getMeetingInfo_week(request):
    result = {}
    for i in range(1,6):
        tmp1 = {}
        tmp1["location"] = i
        for j in range(1,8):
            tmp2 = {}
            tmp2["meeting"] = []
            tmp1[j] = tmp2
        result[i] = tmp1

    data = Meeting.objects.all()
    for i in range(len(data)):
        # 抓該日期的 meeting 資料
        if(int(data[i].start[5:7]) == int(request.POST['month'])):
            if(data[i].room == 'Room1'):
                if(int(data[i].start[8:10]) == (int(request.POST['day']) + 0)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][1]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == (int(request.POST['day']) + 1)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][2]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == (int(request.POST['day']) + 2)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][3]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == (int(request.POST['day']) + 3)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][4]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == (int(request.POST['day']) + 4)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][5]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == (int(request.POST['day']) + 5)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][6]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == (int(request.POST['day']) + 6)):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[1][7]["meeting"].append(tmp_dict)
            elif(data[i].room == 'Room2'):
                if(int(data[i].start[8:10]) == int(request.POST['day']) + 0):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][1]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 1):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][2]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 2):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][3]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 3):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][4]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 4):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][5]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 5):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][6]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 6):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[2][7]["meeting"].append(tmp_dict)
            elif(data[i].room == 'Room3'):
                if(int(data[i].start[8:10]) == int(request.POST['day']) + 0):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][1]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 1):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][2]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 2):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][3]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 3):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][4]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 4):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][5]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 5):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][6]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 6):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[3][7]["meeting"].append(tmp_dict)
            elif(data[i].room == 'Room4'):
                if(int(data[i].start[8:10]) == int(request.POST['day']) + 0):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][1]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 1):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][2]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 2):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][3]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 3):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][4]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 4):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][5]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 5):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][6]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 6):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[4][7]["meeting"].append(tmp_dict)
            elif(data[i].room == 'Room5'):
                if(int(data[i].start[8:10]) == int(request.POST['day']) + 0):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][1]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 1):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][2]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 2):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][3]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 3):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][4]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 4):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][5]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 5):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][6]["meeting"].append(tmp_dict)
                elif(int(data[i].start[8:10]) == int(request.POST['day']) + 6):
                    tmp_dict = {}
                    tmp_dict["topic"] = data[i].topic
                    tmp_dict["host"] = data[i].host
                    tmp_dict["start"] = data[i].start
                    tmp_dict["end"] = data[i].end
                    tmp_dict["attendee"] = data[i].attendee
                    tmp_dict["room"] = data[i].room
                    result[5][7]["meeting"].append(tmp_dict)
    return JsonResponse(result, safe=False)

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, timedelta
SCOPES = ['https://www.googleapis.com/auth/calendar']

@csrf_exempt
def createReminder(request):
    id = request.POST['id']#會議ID
    reminderTime = request.POST['reminder_time']#幾分鐘前提醒
    meeting = Meeting.objects.get(pk=id)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    # 會跳出視窗要求使用者給權限
    # 若是要更換使用者create google reminder，請把token.pickle刪除，否則會寫到上一個使用者的google calendar
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\\Users\\gtr51\\Documents\\MyStudio\\Project\\Meeting Room Management\\website\\current\\prduction server\\Virtual_room_backend\\room\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': meeting.topic,
        'location': meeting.room,
        'start': {
            'dateTime': meeting.start + ':00',
            'timeZone': 'Asia/Taipei',
        },
        'end': {
            'dateTime': meeting.end + ':00',
            'timeZone': 'Asia/Taipei',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': reminderTime},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
    return JsonResponse({'result': 0})

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
    meeting = Meeting.objects.filter(topic = topic, host = host, start = start, end = end)[0]
    return JsonResponse({"result":0, 'id': meeting.pk}, safe=False)

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
    return JsonResponse({'result':0})

@csrf_exempt
def meeting_delete_view(request):
    meeting = Meeting.objects.get(pk=request.POST['id'])
    meeting.delete()
    return JsonResponse({'result':0})
