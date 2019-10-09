from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('',views.index,name="index"),
    path('delete/<int:post_id>',views.delete,name="delete"),
    path("like/<int:post_id>",views.like,name="like"),
    path('dislike/<int:post_id>',views.dislike,name="dislike"),
]