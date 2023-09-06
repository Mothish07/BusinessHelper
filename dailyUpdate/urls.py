from django.urls import path

from dailyUpdate import views

urlpatterns = [
   path('',views.dailyupdatesfunc,name = 'dailyUpdatesFunction'),
  
]
