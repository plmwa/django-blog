from django.test import TestCase
from django.urls import reverse

from ..models import Post

class IndexTests(TestCase):
  """IndexViewのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('blog:index'))
    self.assertEqual(response.status_code, 200)

class PostListTests(TestCase):

  def setUp(self):
    """
    テスト環境の準備用メソッド。名前は必ず「setUp」とすること。
    同じテストクラス内で共通で使いたいデータがある場合にここで作成する。
    """
    post1 = Post.objects.create(title='title1', text='text1')
    post2 = Post.objects.create(title='title2', text='text2')

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('blog:post_list'))
    self.assertEqual(response.status_code, 200)
  
  def test_get_2posts_by_list(self):
    """GET でアクセス時に、setUp メソッドで追加した 2件追加が返されることを確認"""
    response = self.client.get(reverse('blog:post_list'))
    self.assertEqual(response.status_code, 200)
    self.assertQuerysetEqual(
      # Postモデルでは __str__ の結果としてタイトルを返す設定なので、返されるタイトルが投稿通りになっているかを確認
      response.context['post_list'],
      ['<Post: title1>', '<Post: title2>'],
      ordered = False # 順序は無視するよう指定
    )
    self.assertContains(response, 'title1') # html 内に post1 の title が含まれていることを確認
    self.assertContains(response, 'title2') # html 内に post2 の title が含まれていることを確認

  def tearDown(self):
      """
      setUp で追加したデータを消す、掃除用メソッド。
      create とはなっているがメソッド名を「tearDown」とすることで setUp と逆の処理を行ってくれる＝消してくれる。
      """
      post1 = Post.objects.create(title='title1', text='text1')
      post2 = Post.objects.create(title='title2', text='text2')

class PostCreateTests(TestCase):
    """PostCreateビューのテストクラス."""

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_with_data(self):
        """適当なデータで POST すると、成功してリダイレクトされることを確認"""
        data = {
            'title': 'test_title',
            'text': 'test_text',
        }
        response = self.client.post(reverse('blog:post_create'), data=data)
        self.assertEqual(response.status_code, 302)
    
    def test_post_null(self):
        """空のデータで POST を行うとリダイレクトも無く 200 だけ返されることを確認"""
        data = {}
        response = self.client.post(reverse('blog:post_create'), data=data)
        self.assertEqual(response.status_code, 200)