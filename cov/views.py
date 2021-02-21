from django.shortcuts import render
from . import utils
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import datetime


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

def china(request):
    print(">>>china")
    return render(request, 'china.html')

def get_l1_data_china(self):
    print(">>>get_l1_data_china")
    data = utils.get_l1_data_china()
    # print("data[:10]",data[:10])
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[:]:
        day.append(a.strftime("%m-%d"))
        # a是datetime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return JsonResponse({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})

def get_l2_data_china(self):
    data = utils.get_l2_data_china()
    day, confirm_add, suspect_add, heal_add,dead_add= [], [], [],[], []
    # print(">>>get_l2_data_china data",data)
    for a, b, c, d, e in data[:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        # 处理异常数据，负值直接取零
        b = b if b > 0 else 0
        c = c if c > 0 else 0
        d = d if d > 0 else 0
        e = e if e > 0 else 0
        confirm_add.append(b)
        suspect_add.append(c)
        heal_add.append(d)
        dead_add.append(e)
    return JsonResponse({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add})

def get_c1_data_china(self):
    print(">>>get_c1_data_china")
    res = []
    for tup in utils.get_c1_data_china():
        # print(tup)
        res.append({"dateId":tup[0],"confirmedCount":int(tup[1]),"suspectedCount":int(tup[5]),
                    "curedCount":int(tup[3]),"deadCount":int(tup[7])})
    return JsonResponse({"data":res})

def get_c2_data_china(self):
    res = []
    dateIdlst = []
    provlst = []
    # 还是用c1
    data = utils.get_c2_data_china()
    print(">>>get_l2_data_china data[:10]",data[:10])
    # 省份列表
    provlist = ["AH","AM","BJ","CQ","FJ","GD","GS","GX","GZ","HB","HB-1","HLJ","HN","HN-1","HN-2","JL","JS","JX","LN","NMG","NX","QH","SC","SD","SH","SX","SX-1","TJ","TW","XG","XJ","XZ","YN","ZJ"]
    day = []
    provname = []
    provcode = []
    confirm = []
    for a, b, c, d in data[:]:
        # if a.strftime("%y-%m-%d") == '20-01-29': # 34
        #     print("20-01-29")
        # 20:4,21:9,22:21,23:31,24:32,25-28:33,29:34
        # ymd = a.strftime("%y-%m-%d")
        # if ymd != '20-01-20' and ymd != '20-01-21' and ymd != '20-01-22' and ymd != '20-01-23'\
        # and ymd != '20-01-24' and ymd != '20-01-25' and ymd != '20-01-26' and ymd != '20-01-27' and ymd != '20-01-28': # 33
        # 跳过1月份有缺失的数据
        if a.strftime("%y-%m") != '20-01':
            # print(ymd)
            day.append(a.strftime("%m-%d"))  # a是datatime类型
            # 处理异常数据，负值直接取零
            d = d if d > 0 else 0
            provname.append(b)
            provcode.append(c)
            confirm.append(d)
    # print(len(day))
    # print(len(provname))
    # print(len(provcode))
    # print(len(confirm))
    day = day[:368] # 取前368天即可
    data0 = [] # 二维数组
    # 一共368天
    for i in range(368):
        a = provname[i::368]
        b = confirm[i::368]
        # if i < 3:
        #     print(i,len(a),day[i::368])
        data1 = []
        for j in range(len(a)):
            # print(j, a[j])
            data1.append({"name": a[j], "value": b[j]})
        # print("data1",data1)
        data0.append(data1)
    # print(data[:5])
    # cnt = 0
    # for tup in utils.get_c2_data_china():
    #     if cnt < 10:
    #         print(tup)
    #     # date = str(tup[0]).split()[:10][0]
    #     # # print(date)
    #     # dateIdlst.append({"dateId":date})
    #     # provlst.append({"name":tup[1],"value":int(tup[2])})
    #     # res.append({"dateId":date,"provinceName":tup[1],"confirmedCount":int(tup[2]),"suspectedCount":int(tup[6]),
    #     #             "curedCount":int(tup[4]),"deadCount":int(tup[8])})
    #     cnt = cnt + 1
    res = []
    for tup in utils.get_c1_data_china(): # 补零
        # print(tup)
        if tup[0].strftime("%y-%m") != '20-01':
            res.append({"dateId":tup[0].strftime("%y-%m"),"confirmedCount":int(tup[1]),"suspectedCount":int(tup[5]),
                        "curedCount":int(tup[3]),"deadCount":int(tup[7])})
    for k in range(368-349):
        res.append({"dateId": 0, "confirmedCount": 0, "suspectedCount": 0,
                    "curedCount": 0, "deadCount": 0})
    return JsonResponse({"data":data0,"day":day, "res":res})
