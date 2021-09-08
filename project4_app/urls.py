from django.contrib import admin
from django.urls import path
from project4_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='empty'),

]
