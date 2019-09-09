from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, create_an_item, edit_item, toggle_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list),
    path('add', create_an_item),
    path('edit/<int:item_id>', edit_item),
    path('toggle/<int:item_id>', toggle_status),
]
