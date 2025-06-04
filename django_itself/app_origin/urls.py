from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import path
from . import views

# Create a staff required decorator
staff_required = user_passes_test(lambda u: u.is_staff, login_url='/admin/login')

urlpatterns = [
    path('', views.NewsListViewForAll.as_view(), name='news_list_for_all'),
    
    # Wrap admin views with staff_required decorator
    path('list/', staff_required(views.NewsListView.as_view()), name='news_list'),
    path('new/', staff_required(views.NewsCreateView.as_view()), name='news_create'),
    path('<int:pk>/edit/', staff_required(views.NewsUpdateView.as_view()), name='news_update'),
    path('<int:pk>/delete/', staff_required(views.NewsDeleteView.as_view()), name='news_delete'),
]