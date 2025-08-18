from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post),
    path('post/post-details/', views.post_details)
]

