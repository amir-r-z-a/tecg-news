from django.urls import path
from . import views
urlpatterns = [
    path('news/', views.news_list),
    path('news/<int:pk>/', views.news_detail),
    path('news/<str:tag>/', views.filter_tag),
]