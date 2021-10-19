#!/usr/bin/env python
# encoding: utf-8

from django.urls import path
from . import views

urlpatterns = [
    
    path('item_table.html', views.item_table, name='item_table'),
    path('add_item.html', views.add_item, name='add_item'),
    path('del_item/<int:item_id>', views.del_item, name='del_item'),
    path('update_item/<int:item_id>', views.update_item, name='update_item'),
    
]
