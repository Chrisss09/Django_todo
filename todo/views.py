from django.shortcuts import render

def get_todo_list(request):
    return render(request, 'todo_list.html')