from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.home,name="home"),
    path('description/<pid>',views.description,name="description"),
    path('edit/<pid>', views.taskedit,name="taskedit"),
    path('delete/<pid>', views.taskdelete,name="taskdelete"),

]
