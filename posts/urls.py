from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post),
    path('post-details/<int:id>/', views.post_details)
]

