from django.urls import path

from purchaseUpdates import views

urlpatterns = [
   path('',views.purchaseupdatesfunc,name = 'purchaseUpdatesFunction'),
  
]