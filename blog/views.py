from django.shortcuts import render

posts = [
        {
        'author': 'Varun 1',
        'title': 'Blog Post 1',
        'content' : 'First blog post content',
        'date_posted' : 'October 1, 2018'
        },
        {
        'author': 'Varun 2',
        'title': 'Blog Post 2',
        'content' : 'Second blog post content',
        'date_posted' : 'October 2, 2018'
        },

]

def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
