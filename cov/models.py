from django.db import models

class Details(models.Model): # 详情表
    update_time = models.DateTimeField(blank=True, null=True)           # 数据最后更新时间
    province = models.CharField(max_length=50, blank=True, null=True)   # 省
    city = models.CharField(max_length=50, blank=True, null=True)       # 市
    confirm = models.IntegerField(blank=True, null=True)                # 累计确诊
    confirm_add = models.IntegerField(blank=True, null=True)            # 新增确诊
    heal = models.IntegerField(blank=True, null=True)                   # 累计治愈
    dead = models.IntegerField(blank=True, null=True)                   # 累计死亡

    # 主键为id
    class Meta:
        managed = True
        db_table = 'details'


class History(models.Model):
    ds = models.DateTimeField(primary_key=True)                         # 日期
    confirm = models.IntegerField(blank=True, null=True)                # 累计确诊
    confirm_add = models.IntegerField(blank=True, null=True)            # 当日新增确诊
    suspect = models.IntegerField(blank=True, null=True)                # 剩余疑似
    suspect_add = models.IntegerField(blank=True, null=True)            # 当日新增疑似
    heal = models.IntegerField(blank=True, null=True)                   # 累计治愈
    heal_add = models.IntegerField(blank=True, null=True)               # 当日新增治愈
    dead = models.IntegerField(blank=True, null=True)                   # 累计死亡
    dead_add = models.IntegerField(blank=True, null=True)               # 当日新增死亡

    class Meta:
        managed = True
        db_table = 'history'

class History_China(models.Model):
    dateId = models.DateTimeField(blank=True, null=True)                    # 日期
    confirmedCount = models.IntegerField(blank=True, null=True)             # 累计确诊
    confirmedIncr = models.IntegerField(blank=True, null=True)              # 新增确诊
    curedCount = models.IntegerField(blank=True, null=True)                 # 累计治愈
    curedIncr = models.IntegerField(blank=True, null=True)                  # 新增治愈
    currentConfirmedCount = models.IntegerField(blank=True, null=True)      # 累计现有确诊
    currentConfirmedIncr = models.IntegerField(blank=True, null=True)       # 新增现有确诊
    deadCount = models.IntegerField(blank=True, null=True)                  # 累计死亡
    deadIncr = models.IntegerField(blank=True, null=True)                   # 新增死亡
    suspectedCount = models.IntegerField(blank=True, null=True)             # 累计疑似
    suspectedCountIncr = models.IntegerField(blank=True, null=True)         # 新增疑似

    class Meta:
        managed = True
        db_table = 'history_china'


class History_China_Prov(models.Model):
    dateId = models.DateTimeField(blank=True, null=True)                    # 日期
    provinceName = models.CharField(max_length=50, blank=True, null=True)   # 省
    provinceCode = models.CharField(max_length=50, blank=True, null=True)   # 省代码
    confirmedCount = models.IntegerField(blank=True, null=True)             # 累计确诊
    confirmedIncr = models.IntegerField(blank=True, null=True)              # 新增确诊
    curedCount = models.IntegerField(blank=True, null=True)                 # 累计治愈
    curedIncr = models.IntegerField(blank=True, null=True)                  # 新增治愈
    currentConfirmedCount = models.IntegerField(blank=True, null=True)      # 累计现有确诊
    currentConfirmedIncr = models.IntegerField(blank=True, null=True)       # 新增现有确诊
    deadCount = models.IntegerField(blank=True, null=True)                  # 累计死亡
    deadIncr = models.IntegerField(blank=True, null=True)                   # 新增死亡
    suspectedCount = models.IntegerField(blank=True, null=True)             # 累计疑似
    suspectedCountIncr = models.IntegerField(blank=True, null=True)         # 新增疑似

    class Meta:
        managed = True
        db_table = 'history_china_prov'
