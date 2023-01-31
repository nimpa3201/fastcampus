from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)
class Menu(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=20)

class Order(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    order_date = models.DateTimeField('date order')
    address = models.CharField(max_length=40) 
    estimated_time =models.BigIntegerField(default=-1 ) # 배달예상시간.. 사장님이 입력하기전 기본값 -1 
    deliver_finish =models.BooleanField(default=0) #배달 됐는지 안됐는지 boolen값

class Orderfood(models.Model):
    order =models.ForeignKey(Order,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)



# Create your models here.
