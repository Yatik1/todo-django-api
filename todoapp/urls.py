from django.urls import path
from . import views
from .viewsets import TodoViewSet

urlpatterns =[
    path("",views.start_app),
    path("all/",views.all_todos),
    path("all_view/", TodoViewSet.as_view({'get':'list'})),
    path("post/",views.post_todo),
    path("update/<int:pk>/",views.update_todo),
    path("delete/<int:pk>/",views.delete_todo),
]