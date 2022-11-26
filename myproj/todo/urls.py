from django.urls import path
from . import views

app_name="todo"
urlpatterns=[
    path('', views.view, name='view'),
    path('add', views.add, name='add'),
    path('dlt/<int:pk>', views.dlt, name='dlt'),
]