from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from .forms import ToDoForm
# Create your views here.
def home(request):
    todo_list = ToDo.objects.all()
    #print(todo_list)
    form = ToDoForm()
    context = {'app_name':'Todo App', 'todo_list':todo_list,'form':form}
    return render(request, 'home.html', context)

def todo_view(request):
    # form = ToDoForm
    # context = {'form':form}
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            text = request.POST.get('todo_text')
            ToDo.objects.create(todo_text = text)
    return redirect('home')