from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<item_id>', views.delete, name="delete"),
    path('cross_off/<item_id>', views.cross_off, name="cross_off"),
    path('uncross/<item_id>', views.uncross, name="uncross"),
]
