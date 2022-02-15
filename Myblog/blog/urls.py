from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index,name='blog_index'),
    path('add/',views.blog_add,name='blog_add'),
    path('list/',views.list,name='blog_list'),
    path('detail/<blog_id>/',views.detail,name='blog_detail'),
    path('delete/<blog_id>/',views.delete,name='blog_delete'),
    path('update/<blog_id>/',views.update,name='blog_update'),
]