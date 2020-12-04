from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from .forms import ToDoForm

def home(request):
    todo_list = ToDo.objects.all()
    form = ToDoForm()
    context = {'app_name':'Todo App', 'todo_list':todo_list,'form':form}
    return render(request, 'home.html', context)

def todo_view(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('todo_text')
            # text = request.POST.get('todo_text')
            ToDo.objects.create(todo_text = text)
    return redirect('home')

def edit_view(request, pk):
    # return HttpResponse("ho")
    todo_obj = ToDo.objects.get(pk = pk)
    print(todo_obj)
    form = ToDoForm(instance = todo_obj)
    context = {'form':form,'todo_obj': todo_obj}
    print(form)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance = todo_obj)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'edit.html', context)
          


 
def delete_view(request, pk):
    # return HttpResponse("ho")
    if request.method == 'POST':
        todo_obj = ToDo.objects.get(pk = pk)
        todo_obj.delete()
    return redirect('home')