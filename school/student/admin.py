from django.contrib import admin

# Register your models here.

#要使用的Model
from .models import student

#後台編輯表單相關參數設定
class studentAdmin (admin.ModelAdmin):
    #要顯示的列表欄位
    list_display = ('id', 'account', 'name', 'gender', 'born', 'email', 'phone')

    #過濾器要過濾的欄位
    list_filter = ('country', 'city', 'area')

    #搜尋時參照的欄位
    search_fields = ('account', 'name', 'email')

    #編輯時可供編輯欄位
    fields = ('name', 'born', 'email', 'phone', 'country', 'city', 'area', 'address', 'zip')

    #依欄位做排序
    ordering = ('id',)

#要註冊的Model與後台編輯表單
admin.site.register(student, studentAdmin)
