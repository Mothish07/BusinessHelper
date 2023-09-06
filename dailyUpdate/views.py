from django.shortcuts import render
from . models import daily_Update
from datetime import date
# Create your views here.
def dailyupdatesfunc(request):
    dateupdate = date.today()
    if request.method == 'POST':
        sales = request.POST['sales']
        spend = request.POST['spend']
        duObj = daily_Update(sales=sales,spend=spend)
        duObj.save()
   
    return render(request,'dailyUpdate/dailyupdate.html',{'date':dateupdate})
    
