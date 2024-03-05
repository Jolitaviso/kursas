from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    path('<int:pk>/comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    path('<int:pk>/like/', views.PostLikeCreate.as_view()),
    path('<int:pk>/like/', views.CommentLikeCreate.as_view()),
    path('signup/', views.UserCreate.as_view()),
    path('die/', views.UserDelete.as_view()),
]


    # path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    # path('posts/<int:pk>/like', views.PostLikeCreate.as_view()),