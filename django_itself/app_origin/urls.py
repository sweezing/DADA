from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('new/', views.NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
]