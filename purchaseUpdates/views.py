from django.shortcuts import render
from . models import purchase_Update
from datetime import date
# Create your views here.
def purchaseupdatesfunc(request):
    dateupdate = date.today()
    if request.method == 'POST':
        shopName = request.POST['shopName']
        price = request.POST['price']
        puObj = purchase_Update(shopName=shopName, price= price)
        puObj.save()
   
    return render(request,'purchaseUpdates/purchaseupdate.html',{'date':dateupdate})
