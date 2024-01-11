from django.urls import path
from .import views
urlpatterns = [
    path('',views.home),
    path('1',views.index),
    path('3',views.p3),
    path('add',views.add),
    path('trio',views.trigo),

]