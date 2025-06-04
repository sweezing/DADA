from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Add this

from .models import News
from .forms import NewsForm

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin that requires user to be logged in and have staff status"""
    login_url = '/admin/login'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect(self.login_url + '?next=' + self.request.path)


# Public view (no restriction)

class NewsListViewForAll(ListView):
    model = News 
    template_name = 'magazine/news_list_for_all.html'
    context_object_name = 'news'

# Only admin

class NewsListView(AdminRequiredMixin, ListView):
    model = News 
    template_name = 'magazine/news_list.html'
    context_object_name = 'news'

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