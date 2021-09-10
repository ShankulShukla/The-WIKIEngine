from flask import Flask, render_template, request
from wikiSearch import fetchResult

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html', key="")

@app.route('/search',methods = ['Post'])
def searchResult():
    keyword = request.form['keyword']
    a, b, c, d, e, f = fetchResult(keyword)
    return render_template('homepage.html', key=keyword, res_l1=a, res_l2=b, res_l3=c, imgres_l1=d, imgres_l2=e, imgres_l3=f)

if __name__ == '__main__':
    app.run(debug=True)