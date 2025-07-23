from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView , DetailView , View , TemplateView

from blog.models import Article , Category , Tag , Comment
from mixins import *

class ArticleListView(ListView):
    template_name = 'blog/blog.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 6
    def get_queryset(self):
        return Article.objects.filter(is_publish=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_articles'] = Article.objects.filter(is_publish=True)[:2]
        context['category'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context
    
class ArticleDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Article
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_articles'] = Article.objects.filter(is_publish=True)[:2]
        context['category'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context

class CategoryArtList(View):
    template_name = 'blog/blog.html'
    def get(self , request , id):
        category = get_object_or_404(Category , id=id)
        articles = category.articles_cate.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        recent_articles = Article.objects.filter(is_publish=True)[:2]
        return render(request , self.template_name , {'articles':articles , 'category':categories , 'tags':tags , 'recent_articles':recent_articles})

class TagArtList(View):
    template_name = 'blog/blog.html'
    def get(self , request , id):
        tag = get_object_or_404(Tag , id=id)
        articles = tag.article_tag.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        recent_articles = Article.objects.filter(is_publish=True)[:2]
        return render(request , self.template_name , {'articles':articles , 'category':categories , 'tags':tags , 'recent_articles':recent_articles})
    
class SearchBox(TemplateView):
    queryset = None
    template_name = "blog/blog.html"
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset =  Article.objects.filter(title__icontains = q)
        categories = Category.objects.all()
        tags = Tag.objects.all()
        recent_articles = Article.objects.filter(is_publish=True)[:2]
        return render(request , self.template_name , {'articles':queryset , 'category':categories , 'tags':tags , 'recent_articles':recent_articles})
    
class CommentView(LogoutRequirdMixins , View):
    def post(self , request , pk):
        art = Article.objects.get(id=pk)
        user = request.user
        message = request.POST.get('message')
        Comment.objects.create(user=user , article=art , message=message)
        return redirect('blog:article_detail' , pk)