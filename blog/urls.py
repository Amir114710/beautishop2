from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('' , ArticleListView.as_view() , name='article_list'),
    path('blog_detail/<int:pk>' , ArticleDetailView.as_view() , name='article_detail'),
    path('category/<int:id>' , CategoryArtList.as_view() , name='category_art'),
    path('tag/<int:id>' , TagArtList.as_view() , name='tag_art'),
    path('comment/<int:pk>' , CommentView.as_view() , name='comment'),
]