from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post, name='post'),
    path('post-details/<int:post_id>/', views.post_details,name='post_details'),
]

