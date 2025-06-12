from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Add this
from django.contrib.auth.views import LogoutView as DjangoLogoutView

from .models import News
from .forms import NewsForm

class AuthRequiredMixin(LoginRequiredMixin):
    """Mixin that requires user to be logged in"""
    login_url = '/accounts/login/'  # укажите ваш URL для входа
    
    def handle_no_permission(self):
        return redirect(self.login_url + '?next=' + self.request.path)

class AdminRequiredMixin(AuthRequiredMixin, UserPassesTestMixin):
    """Mixin that requires user to be staff"""
    def test_func(self):
        return self.request.user.is_staff


# Public view (no restriction) - для всех, включая анонимных пользователей
class NewsListViewForAll(ListView):
    model = News 
    template_name = 'magazine/news_list_for_all.html'
    context_object_name = 'news'

# Для аутентифицированных пользователей (не обязательно staff)
class NewsListView(LoginRequiredMixin, ListView):
    model = News 
    template_name = 'magazine/news_list.html'
    context_object_name = 'news'

# Только для администраторов (staff)
class NewsCreateView(AdminRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'magazine/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsUpdateView(AdminRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'magazine/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(AdminRequiredMixin, DeleteView):
    model = News
    template_name = 'magazine/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')

# Allow GET method for logout so users can log out via simple link
class LogoutView(DjangoLogoutView):
    next_page = 'news_list_for_all'
    http_method_names = ['get', 'post', 'head', 'options', 'trace']