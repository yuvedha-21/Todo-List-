from django import views
from django.shortcuts import redirect, render
from django.views import View
# Create your views here.
from .models import Mytodos
from .forms import Todoform

class Home(View):
    def get(self,request):
        return render(request,'home.html')

def alltodos(request):
    tasks=Mytodos.objects.all()
    form=Todoform()
    if request.method =='POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'alltodos.html',{'tasks':tasks,'form':form})

def deleteitem(request,pk):
    task=Mytodos.objects.get(id=pk)    
    task.delete()
    return redirect('alltodos')

def updateitem(request,pk):
    todo=Mytodos.objects.get(id=pk)
    updateform=Todoform(instance=todo)
    if request.method == 'POST':
        updateform = Todoform(request.POST,instance = todo)
        if updateform.is_valid():
            updateform.save()
            return redirect('alltodos')

    return render(request,'updateitem.html',{'todo':todo,'updateform':updateform})   