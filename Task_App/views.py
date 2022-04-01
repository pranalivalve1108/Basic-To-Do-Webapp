from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import List_Database

# Create your views here.
def a(request):
    if request.method=='POST':
        r3=request.POST.get('id')
        r1=request.POST.get('title')
        r2=request.POST.get('description')
        object_render=List_Database(id=r3,Title=r1,Description=r2)
        object_render.save()
    obj_show=List_Database.objects.all()
    return render(request,'To-Do-List.html',{'a_key':obj_show})

def d_data(request,valve):
    d_obj=List_Database.objects.get(id=valve) 
    d1_obj=List_Database.objects.all()
    d_obj.delete()
    return render(request,'delete_data.html',{'d_key':d_obj,'d1_key':d1_obj})
           
 