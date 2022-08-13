from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
from .models import Task


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task2'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task2'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task2'
    fields = ('task','priority','date')

    def get_success_url(self):
     return reverse_lazy('todoapp:cbvdetail',kwargs={'pk': self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')
def home(request):
    task2 = Task.objects.all()
    if request.method == "POST":
        task= request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=Task(task=task,priority=priority,date=date)
        task1.save()
        return redirect('/')

    return render(request,'home.html',{"task2":task2})

def delete(request,id):
    delt=Task.objects.get(id=id)
    if request.method=="POST":
            delt.delete()
            return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task1 =Task.objects.get(id=id)
    form =TodoForms(request.POST or None,instance=task1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{"form": form,'task1': task1})