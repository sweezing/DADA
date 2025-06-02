from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import News
from .forms import NewsForm

### MAIN CLASSES ### 

class NewsListView(ListView):
    model = News 
    template_name = 'magazine/news_list.html'
    context_object_name = 'news'

class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'magazine/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'magazine/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'magazine/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')
    
    # def delete_image(self, request, *args, **kwargs):
    #     self.news = self.get_object()
    #     if self.object.image:
    #         self.object.image.delete(save=False)
    #     return super().delete(request, *args, **kwargs)