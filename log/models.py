from django.db import models

# Create your models here.
class LogItem(models.Model):
    #處理進度的許項清單
  ST_OPTIONS=[
      (0,'待處理'),
      (1,'處理中'),
      (2,'已結案'),
  ]
#報修主旨
  subject=models.CharField('報修主旨', max_length=255)
#報修內容
  discription=models.TextField('報修內容')
#報修人
  reporter=models.CharField('報修人',max_length=30)
#連絡電話
  phone=models.CharField('連絡電話',max_length=30)
#報修時間
  ctime=models.DateTimeField(auto_now_add=True)
#-------------------------------------------
#處理人員
  handler=models.CharField('處理人員',max_length=30)
  #處理進度
  status=models.IntegerField(
                '處理速度',
                default=0,
                choices=ST_OPTIONS
            )
#處理說明
  comment=models.TextField('處理說明')
#更新時間
  utime=models.DateTimeField('更新時間',auto_now=True)
 # 照片
  picture = models.ImageField('照片', blank=True, null=True)
  def __str__(self):
    return self.reporter+':'+self.subject
   
  def get_status_class(self):
    return ['danger', 'warning', 'success'][self.status]