#設計models.py
from django.db import models

#以學生資料表做範例
class student(models.Model):
  name = models.CharField('姓名', max_length=20, null=False)
  gender = models.CharField('性別', max_length=1, default='0', null=False)
  account = models.CharField('帳號', max_length=20, null=False)
  password = models.CharField('密碼', max_length=50, null=False)
  born = models.DateField('生日', null=False)
  email = models.EmailField('信箱', max_length=255, blank=True, default='')
  phone = models.CharField('電話', max_length=20, blank=True, default='')
  country = models.CharField('國家', max_length=5, blank=True, default='TW')
  city = models.CharField('城市', max_length=30, blank=True, default='Taipei')
  area = models.CharField('區域', max_length=30, blank=True, default='')
  address = models.CharField('地址', max_length=200, blank=True, default='')
  zip = models.CharField('郵遞區號', max_length=5, blank=True, default='')

  #後台管理介面中，顯示的欄位
  def __str__(self):
    return self.name

  #資料表定羕
  class Meta:
        db_table = 'student' #資料表名稱
