import unittest
from app.models import NewsArticle

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticle class
    '''

    def setUp(self):
        '''
        Set up method that runs before every Test
        '''

        self.new_article = NewsArticle("Python","Nakish",'Python Must Be Crazy','A thrilling new Python Series','https://blablabla',"imageToUrl","2020-04-04")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticle))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_article.name,'Python')
        self.assertEqual(self.new_article.description,'A thrilling new Python Series')
        self.assertEqual(self.new_article.url,'https://newsapi.org/v2/sources?apiKey=63a6e13ee20244429ff2fa72529d69c5')
        self.assertEqual(self.new_article.author,"lucky")
        self.assertEqual(self.new_article.title,"Python Must Be Crazy")
        self.assertEqual(self.new_article.urlToImage,"urlToImage")
        self.assertEqual(self.new_article.publishedAt,"2020-04-04")