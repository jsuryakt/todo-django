from django.contrib import admin
from django.urls import path
from maketodo.views import home, todo_view, edit_view, delete_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_todo/', todo_view, name='adding_todo'),
    path('edit_todo/<int:pk>', edit_view, name='edit_todo'),
    path('delete_todo/<int:pk>', delete_view, name='delete_todo'),
]
