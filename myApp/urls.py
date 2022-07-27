from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = 'index'),
    path("addStudent/",views.addStudent, name = 'addStudent'),
    
    path("update/<str:id>",views.update, name = 'update'),
    
    path("delete/<str:id>",views.delete, name = 'delete'),

]
