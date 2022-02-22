from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_list', views.PostListView.as_view(), name='post_list'), # ここを追加
    path('post_create', views.PostCreateView.as_view(), name='post_create'), # 追加

]