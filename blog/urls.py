from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,

    ActListView,
    ActDetailView,
    ActCreateView,
    ActUpdateView,
    ActDeleteView,
    UserActListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

# for activity page
    path('activity/', ActListView.as_view(), name='blog-activity'),

    path('user/<str:username>/act', UserActListView.as_view(), name='user-acts'),
    path('activity/<int:pk>/', ActDetailView.as_view(), name='act-detail'),
    path('activity/new/', ActCreateView.as_view(), name='act-create'),
    path('activity/<int:pk>/update/', ActUpdateView.as_view(), name='act-update'),
    path('activity/<int:pk>/delete/', ActDeleteView.as_view(), name='act-delete'),
# for exploration page
    path('exploration/', views.exploration, name='blog-exploration'),

#for comment setting
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
