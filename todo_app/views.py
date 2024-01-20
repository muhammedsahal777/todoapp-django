from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .form import editTask
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name='home.html'
    context_object_name ='results'

class DetailedView(DetailView):
    model=Task
    template_name = 'detailed.html'
    context_object_name='result'

class UpdateDetailedView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields =('name' ,'priority' ,'date')
    def get_success_url(self):
        return reverse_lazy('detailedcview', kwargs ={'pk':self.object.id})
    
class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    context_object_name='item'
    success_url=reverse_lazy('homecview')

def home(request):
    obj1 = Task.objects.all()
    if request.method =="POST":
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        if (name and priority and date):
            obj = Task(name=name , priority=priority , date=date)
            obj.save()
            return redirect('/')
    return render(request , 'home.html' , {'results':obj1})


def delete(request,pk):
    element =Task.objects.get(id=pk)
    if request.method=='POST':
        element.delete()
        return redirect('/')
    return render(request , 'delete.html' ,{'item':element})

def update(request,pk):
    element = Task.objects.get(id=pk)    
    form = editTask(request.POST or None , instance=element)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html' , {'form':form})
