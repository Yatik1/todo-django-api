from django.urls import path
from . import views

urlpatterns =[
    path("",views.start_app),
    path("all/",views.all_todos),
    path("post/",views.post_todo),
    path("update/<int:pk>/",views.update_todo),
    path("delete/<int:pk>/",views.delete_todo),
]