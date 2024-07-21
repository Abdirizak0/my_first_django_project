from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    add_comment, profile, dashboard, user_list, change_user_role, register,
    PostViewSet, CommentViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/change-role/', change_user_role, name='change_user_role'),
    path('register/', register, name='register'),
    path('api/', include(router.urls)),
]



