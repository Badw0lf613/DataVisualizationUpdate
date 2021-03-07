from django.contrib import admin
from cov import models

# Register your models here.

@admin.register(models.Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('update_time', 'province', 'city', 'confirm', 'confirm_add', 'heal', 'dead')
    search_fields = ('update_time', 'province', 'city', 'confirm', 'confirm_add', 'heal', 'dead')
    ordering = ('id',)

@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('ds', 'confirm', 'confirm_add', 'suspect', 'suspect_add', 'heal', 'heal_add', 'dead', 'dead_add')
    search_fields = ('ds', 'confirm', 'confirm_add', 'suspect', 'suspect_add', 'heal', 'heal_add', 'dead', 'dead_add')
    ordering = ('ds',)
@admin.register(models.History_China)
class History_ChinaAdmin(admin.ModelAdmin):
    list_display = ('dateId', 'confirmedCount', 'confirmedIncr', 'curedCount', 'curedIncr', 'currentConfirmedCount', 'currentConfirmedIncr', 'deadCount', 'deadIncr', 'suspectedCount', 'suspectedCountIncr')
    search_fields = ('dateId', 'confirmedCount', 'confirmedIncr', 'curedCount', 'curedIncr', 'currentConfirmedCount', 'currentConfirmedIncr', 'deadCount', 'deadIncr', 'suspectedCount', 'suspectedCountIncr')
    ordering = ('id',)
@admin.register(models.History_China_Prov)
class History_China_ProvAdmin(admin.ModelAdmin):
    list_display = ('dateId', 'provinceName', 'provinceCode', 'confirmedCount', 'confirmedIncr', 'curedCount', 'curedIncr', 'currentConfirmedCount', 'currentConfirmedIncr', 'deadCount', 'deadIncr', 'suspectedCount', 'suspectedCountIncr')
    search_fields = ('dateId', 'provinceName', 'provinceCode', 'confirmedCount', 'confirmedIncr', 'curedCount', 'curedIncr', 'currentConfirmedCount', 'currentConfirmedIncr', 'deadCount', 'deadIncr', 'suspectedCount', 'suspectedCountIncr')
    ordering = ('id',)
@admin.register(models.History_Shanghai)
class History_ShanghaiAdmin(admin.ModelAdmin):
    list_display = ('dateId', 'provinceName', 'provinceCode', 'confirmedCount', 'confirmedIncr', 'curedCount', 'curedIncr', 'currentConfirmedCount', 'currentConfirmedIncr', 'deadCount', 'deadIncr', 'suspectedCount', 'suspectedCountIncr')
    search_fields = ('dateId', 'provinceName', 'provinceCode', 'confirmedCount', 'confirmedIncr', 'curedCount', 'curedIncr', 'currentConfirmedCount', 'currentConfirmedIncr', 'deadCount', 'deadIncr', 'suspectedCount', 'suspectedCountIncr')
    ordering = ('dateId',)
@admin.register(models.History_Shanghai_Prov)
class History_Shanghai_ProvAdmin(admin.ModelAdmin):
    list_display = ('provinceName', 'provinceCode', 'cityName', 'confirmedCount', 'curedCount', 'currentConfirmedCount', 'deadCount', 'suspectedCount')
    search_fields = ('provinceName', 'provinceCode', 'cityName', 'confirmedCount', 'curedCount', 'currentConfirmedCount', 'deadCount', 'suspectedCount')
    ordering = ('-confirmedCount',)