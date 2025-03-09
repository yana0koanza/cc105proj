from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm  # Import TaskForm

def task_list(request):
    query = request.GET.get('q', '')
    tasks = Task.objects.filter(title__icontains=query) if query else Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'query': query})

from django.shortcuts import render, redirect
from .models import Task

def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        due_date = request.POST.get("due_date")
        status = request.POST.get("status", "pending")  # ✅ Ensure 'status' is set

        task = Task(title=title, description=description, due_date=due_date, status=status)
        task.save()

        return redirect("task_list")

    return render(request, "tasks/task_form.html")

def task_update(request, id):
    task = get_object_or_404(Task, id=id)  # Fetch the task from the database
    
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description", "")
        task.due_date = request.POST.get("due_date")
        task.save()
        return redirect("task_list")  # Redirect to task list after saving

    return render(request, "tasks/task_form.html", {"task": task})


def task_delete(request, id):
    """Delete a task"""
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

