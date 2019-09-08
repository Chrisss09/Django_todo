from django.shortcuts import render, HttpResponse

def get_todo_list(request):
    return render(request, 'todo_list.html')