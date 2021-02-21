import pymysql
import time
import json
import traceback  #追踪异常
import requests

# 使用腾讯新闻接口，返回历史数据和当日详细数据
def get_tencent_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5' # 当日详细数据
    url_his = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'  # 历史数据

    # 表头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    # 当日详细数据
    r = requests.get(url, headers)
    res = json.loads(r.text)  # json字符串转字典
    data_all = json.loads(res['data'])
    # 历史数据
    r_his = requests.get(url_his, headers)
    res_his = json.loads(r_his.text)
    data_his = json.loads(res_his['data'])
    print(">>>data_his",data_his)
    print(">>>data_all",data_all)
    a = json.dumps(data_all)
    f = open('data_all.json', 'w', encoding='utf-8')
    f.write(a)
    f.close()
    b = json.dumps(data_his)
    f = open('data_his.json', 'w', encoding='utf-8')
    f.write(b)
    f.close()
    # print(">>>data_his chinaDayList",data_his["chinaDayList"])
    history = {}  # 历史数据
    cnt = 0
    for i in data_his["chinaDayList"]:
        ds = i["y"] + "." + i["date"]
        if cnt < 5:
            print(">>>i['date']",i["date"])
            print(">>>ds",ds)
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式为datetime类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
        cnt = cnt + 1
    for i in data_his["chinaDayAddList"]:
        ds = i["y"] + "." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    details = []  # 当日详细数据
    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"]  # 目前只有中国
    data_province = data_country[0]["children"]  # 中国各省
    for pro_infos in data_province:
        province = pro_infos["name"]  # 省名
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details

# 创建连接，创建游标
def get_conn():
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           db="cov",
                           charset="utf8")
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor

# 关闭连接，关闭游标
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# 更新 details 表
def update_details():
    cursor = None
    conn = None
    try:
        li = get_tencent_data()[1]  #  0 是历史数据字典,1 最新详细数据列表
        conn, cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select update_time from details order by id desc limit 1)' #对比当前最大时间戳
        cursor.execute(sql_query,li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()  # 提交事务 update delete insert操作
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

# 插入历史数据
def insert_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]  # 0 是历史数据字典,1 最新详细数据列表
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            # item 格式 {'2020-01-13': {'confirm': 41, 'suspect': 0, 'heal': 0, 'dead': 1}
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),
                                    v.get("suspect_add"), v.get("heal"), v.get("heal_add"),
                                    v.get("dead"), v.get("dead_add")])

        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

# 更新历史数据
def update_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]  #  0 是历史数据字典,1 最新详细数据列表
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds=%s"
        for k, v in dic.items():
            # item 格式 {'2020-01-13': {'confirm': 41, 'suspect': 0, 'heal': 0, 'dead': 1}
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),
                                     v.get("suspect_add"), v.get("heal"), v.get("heal_add"),
                                     v.get("dead"), v.get("dead_add")])
        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

# 获取实时接口数据，数据来源：丁香园，文档http://ncov.leafcoder.cn/docs/#/
def get_ncov_data():
    url_global = 'http://111.231.75.86:8000/api/statistics/latest'  # 最新全球疫情
    url_global_his = 'http://111.231.75.86:8000/api/statistics/' # 历史全球疫情
    url_china_prov_his = 'http://111.231.75.86:8000/api/provinces/CHN/daily/' # 历史中国各省份疫情
    url_china_his = 'http://111.231.75.86:8000/api/countries/daily/?countryNames=中国' # 历史中国疫情
    # 表头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    # 最新全球疫情
    # r = requests.get(url_global, headers)
    # res_global = json.loads(r.text)  # json字符串转字典
    # 历史全球疫情
    # r = requests.get(url_global_his, headers)
    # print("request完毕")
    # res_global_his = json.loads(r.text)  # json字符串转字典
    # print("loads完毕")
    # 历史中国疫情
    r = requests.get(url_china_prov_his, headers)
    print("request完毕")
    res_china_prov_his = json.loads(r.text)  # json字符串转字典
    print("loads完毕")
    a = json.dumps(res_china_prov_his)
    f = open('res_china_prov.json', 'w', encoding='utf-8')
    f.write(a)
    f.close()

# 处理ncov接口的json
def process_json(fname):
    # 省份列表
    provlist = ["AH","AM","BJ","CQ","FJ","GD","GS","GX","GZ","HB","HB-1","HLJ","HN","HN-1","HN-2","JL","JS","JX","LN","NMG","NX","QH","SC","SD","SH","SX","SX-1","TJ","TW","XG","XJ","XZ","YN","ZJ"]
    # 读取json文件
    if fname=='history_china_prov.json':
        f = open(fname, 'r', encoding='utf-8')
        content = f.read()
        lst = json.loads(content)
        print(type(lst))  # list
        print(type(lst[0]))  # dict
        f.close()
        print(len(lst))  # 12844
        details = []  # 详细数据
        for i in lst:
            dateId = i["dateId"]  # 日期
            provinceName = i["provinceName"]  # 省份
            provinceCode = i["provinceCode"] # 省份代码
            confirmedCount = i["confirmedCount"]  # 累计确诊
            confirmedIncr = i["confirmedIncr"]  # 新增确诊
            curedCount = i["curedCount"]  # 累计治愈
            curedIncr = i["curedIncr"]  # 新增治愈
            currentConfirmedCount = i["currentConfirmedCount"]  # 累计现有确诊
            currentConfirmedIncr = i["curedIncr"]  # 新增现有确诊
            deadCount = i["deadCount"]  # 累计死亡
            deadIncr = i["deadIncr"]  # 新增死亡
            suspectedCount = i["suspectedCount"]  # 累计疑似
            suspectedCountIncr = i["suspectedCountIncr"]  # 新增疑似
            details.append(
                [dateId, provinceName, provinceCode, confirmedCount, confirmedIncr, curedCount, curedIncr, currentConfirmedCount,
                 currentConfirmedIncr, deadCount, deadIncr, suspectedCount, suspectedCountIncr])
    elif fname=='history_china.json':
        f = open(fname, 'r', encoding='utf-8')
        content = f.read()
        lst = json.loads(content)
        print(type(lst))  # list
        print(type(lst[0]))  # dict
        f.close()
        print(len(lst))  # 12844
        details = []  # 详细数据
        for i in lst:
            dateId = i["dateId"]  # 日期
            confirmedCount = i["confirmedCount"]  # 累计确诊
            confirmedIncr = i["confirmedIncr"]  # 新增确诊
            curedCount = i["curedCount"]  # 累计治愈
            curedIncr = i["curedIncr"]  # 新增治愈
            currentConfirmedCount = i["currentConfirmedCount"]  # 累计现有确诊
            currentConfirmedIncr = i["curedIncr"]  # 新增现有确诊
            deadCount = i["deadCount"]  # 累计死亡
            deadIncr = i["deadIncr"]  # 新增死亡
            suspectedCount = i["suspectedCount"]  # 累计疑似
            suspectedCountIncr = i["suspectedCountIncr"]  # 新增疑似
            details.append(
                [dateId, confirmedCount, confirmedIncr, curedCount, curedIncr, currentConfirmedCount,
                 currentConfirmedIncr, deadCount, deadIncr, suspectedCount, suspectedCountIncr])
    return details

# 更新 china_history 表
def update_china_history():
    cursor = None
    conn = None
    try:
        li = process_json('history_china.json')  # 返回列表
        conn, cursor = get_conn()
        sql = "insert into history_china(dateId, confirmedCount, confirmedIncr, curedCount, curedIncr, currentConfirmedCount," \
              "currentConfirmedIncr, deadCount, deadIncr, suspectedCount, suspectedCountIncr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(f"{time.asctime()}开始更新最新数据")
        for item in li:
            cursor.execute(sql, item)
        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}更新最新数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

# 更新 china_history_prov 表
def update_china_history_prov():
    cursor = None
    conn = None
    try:
        li = process_json('history_china_prov.json')  # 返回列表
        conn, cursor = get_conn()
        sql = "insert into history_china_prov(dateId, provinceName,provinceCode, confirmedCount, confirmedIncr, curedCount, curedIncr, currentConfirmedCount," \
              "currentConfirmedIncr, deadCount, deadIncr, suspectedCount, suspectedCountIncr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(f"{time.asctime()}开始更新最新数据")
        for item in li:
            cursor.execute(sql, item)
        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}更新最新数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

if __name__ == "__main__":
    #  insert_history()
    # update_history()
    # update_details()
    # get_ncov_data()
    update_china_history()
    # update_china_history_prov()