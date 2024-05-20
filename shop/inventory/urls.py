from django.urls import path
from inventory import views
urlpatterns = [
    path('',views.inventory,name='inventory'),
    path('add',views.add,name='add'),
    path('insert',views.insert,name='insert'),
    path('list',views.list,name='list'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),
]