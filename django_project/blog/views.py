from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#hard coded text
# posts = [
#     {
#     'author': 'number-01',
#     'title': 'Blog Post 1',
#     'content': 'First post content',
#     'date_posted': 'kimtober 27, 2018',
#     },
#     {
#     'author': 'number-11',
#     'title': 'Blog Post 02',
#     'content': 'Second post content',
#     'date_posted': 'kimtober 28, 2018',
#     },
#     ]
def aboutpage(request):
    return HttpResponse('<h1>You overestimate your existance</h1>')

def home(request):
    #creating a dictionary with 'posts' as key
    context = {'title': 'Home','posts': post.objects.all()}
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html [it is expected by convention of listview method]
    context_object_name = 'posts'
    ordering = ['-date_posted'] #[(-)ve sign dictates change in order of date posted]
    #hardcode value to see number of post per page
    paginate_by = 2


class UserPostListView(ListView):
    model = post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html [it is expected by convention of listview method]
    context_object_name = 'posts'
    #hardcode value to see number of post per page
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        #[(-)ve sign dictates change in order of date posted]
        return post.objects.filter(author = user).order_by('-date_posted') 



class PostDetailView(DetailView):
    model = post

    fields = ['title', 'content']

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

    

    

    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form, **kwargs):
        #setting author up before adding content
         form.instance.author = self.request.user
         return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form, **kwargs):
        #setting author up before adding content
         form.instance.author = self.request.user
         return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        #return super().test_func()



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    fields = ['title', 'content']
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





def about(request):

        return render(request, 'blog/about.html',{'title': 'About'} ) #passing title name dynamically



