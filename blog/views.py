from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# def home(request):
#     context = {
#     'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # success_url = '/'  # use this if you want to redirect it to home page

    def form_valid(self, form):
        form.instance.author = self.request.user #setting our author before validating
        return super().form_valid(form) #running the form_valid on parent

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
