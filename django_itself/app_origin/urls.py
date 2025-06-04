from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.NewsListViewForAll.as_view(), name='news_list_for_all'),
    
    # изначально все эти страницы были исключительно для админа
    path('list/', login_required(views.NewsListView.as_view()), name='news_list'),
    path('new/', login_required(views.NewsCreateView.as_view()), name='news_create'),
    path('<int:pk>/edit/', login_required(views.NewsUpdateView.as_view()), name='news_update'),
    path('<int:pk>/delete/', login_required(views.NewsDeleteView.as_view()), name='news_delete'),

        # Встроенные auth-представления Django
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]