from google_play_scraper import Sort, reviews_all
from flask import Flask
from flask_cors import cross_origin
app = Flask(__name__)

@app.route('/playstoreReviews', methods=['POST'])
@cross_origin()
def getReviews():
    result = reviews_all(
        'put your app package name here',
        sleep_milliseconds=0, # defaults to 0
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
        filter_score_with=5 # defaults to None(means all score)
    )
    print(result)
    return str(result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=6734)
