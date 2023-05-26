from django.shortcuts import render
from . models import table
from . models import table2
# Create your views here.
def demo(request):
    obj = table.objects.all()
    obj2 = table2.objects.all()
    return render(request,'index.html',{'ansr':obj,'ansr2':obj2})