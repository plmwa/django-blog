from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IndexView, PostListView

class TestUrls(TestCase):

  """index ページへのURLでアクセスする時のリダイレクトをテスト"""
  def test_post_index_url(self):
    view = resolve('/blog/')
    self.assertEqual(view.func.view_class, IndexView)

  """Post 一覧ページへのリダイレクトをテスト"""
  def test_post_list_url(self):
    view = resolve('/blog/post_list')
    self.assertEqual(view.func.view_class, PostListView)