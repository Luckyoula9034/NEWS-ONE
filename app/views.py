from flask import render_template
from app import app

# Views
@app.route('/news/<news_id')
def index(news_id):

    '''
    View news page function that returns the news details page and its data
    '''

 return render_template('news.html',id = news_id)