from django.shortcuts import render
from . import utils
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


# Create your views here.
def main(request):
    print(">>>main")
    return render(request, 'main.html')

def get_c1_data(self):
    print(">>>get_c1_data")
    data = utils.get_c1_data()
    return JsonResponse({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})


def get_c2_data(self):
    print(">>>get_c2_data")
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return JsonResponse({"data":res})


def get_l1_data(self):
    print(">>>get_l1_data")
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d"))
        #  a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return JsonResponse({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})


def get_l2_data(self):
    print(">>>get_l2_data")
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return JsonResponse({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})


def get_r1_data(self):
    print(">>>get_r1_data")
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return JsonResponse({"city": city, "confirm": confirm})


def get_r2_data(self):
    print(">>>get_r2_data")
    res = []
    for tup in utils.get_r2_data():
        # print(tup)
        res.append({"name": tup[0], "value": int(tup[1])})
    return JsonResponse({"data": res})

def get_time(self):
    return HttpResponse((json.dumps(utils.get_time()))) # 返回的是json