from delivery import views
from django.urls import path,include

urlpatterns = [
    path('orders/',views.order_list,name="order_list")
]
