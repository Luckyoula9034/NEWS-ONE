import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('new@one','Python Must Be Crazy','A thrilling new Python Series','https://www.aftenposten.no/verden/i/oAREbR/trump-holdt-valgmoete-i-nevada-og-trosset-forbud-mot-aa-samle-mange-menn',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()