from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    model = Blog
    paginate_by = 4

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_create_form.html"
    success_url = reverse_lazy('index')
    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request, 'Reserved')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Failed')
        return  super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update_form.html"
    login_url = '/login'

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.kwargs["pk"]})
    def form_valid(self, form):
        messages.success(self.request, 'Reserved')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Failed')
        return  super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('index')
    login_url = '/login'