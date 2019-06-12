from django.shortcuts import render
from testapp.models import *
# Create your views here.
def jaipurjobsinfo(request):
    jaipur_list=jaipurjobs.objects.order_by('date')
    mydict={'joblist':jaipur_list}
    return render(request,'testapp/jaipur.html',context=mydict)
def index(request):
    return render(request,"testapp/index.html")
