from django.urls import path, include
from . import views


urlpatterns = [
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
]
