from django.urls import path
from .views import BookListApiView, BookDetailApiView, BookCreateApiView, BookUpdateApiView, BookDeleteApiView

urlpatterns = [
    path('v1/list/', BookListApiView.as_view()),
    path('v1/detail/<int:pk>/', BookDetailApiView.as_view()),
    path('v1/delete/<int:pk>/', BookDeleteApiView.as_view()),
    path('v1/update/<int:pk>/', BookUpdateApiView.as_view()),
    path('v1/create/', BookCreateApiView.as_view()),
]