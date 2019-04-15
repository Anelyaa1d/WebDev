from django.urls import path, re_path
from api import views
urlpatterns = [
    path('api/tasklist', views.get_task_lists),
    re_path(r'api/tasklist/(\d)/tasks', views.get_tasks),
    re_path(r'api/tasklist/(\d)', views.get_task_list),
]
