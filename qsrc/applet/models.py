from django.db import models


class Urls(models.Model):
    sr_no = models.IntegerField(default=0,primary_key = True)
    prn = models.CharField(max_length=250, default= '2016BTEIT00025')
    links = models.CharField(max_length=2500, default= 'https://www.youtube.com/')
    count = models.IntegerField(default=0)
    primary_key = True

    def __str__(self):
     return str(self.sr_no)+ '---'+ self.prn