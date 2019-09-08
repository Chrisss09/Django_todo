from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, create_an_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list),
    path('add', create_an_item),
]
