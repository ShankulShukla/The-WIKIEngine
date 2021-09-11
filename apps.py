from flask import Flask, render_template, request
from wikiSearch import fetchResult

app = Flask(__name__)

def doYouMean(keyword):
    from nltk.corpus import words
    correct_spellings = words.words()

    from nltk.metrics.distance import jaccard_distance
    from nltk.util import ngrams
    result = ''
    for key in keyword.split():
        if len(key) > 1:
            temp = [(jaccard_distance(set(ngrams(key, 2)), set(ngrams(w, 2))), w) for w in correct_spellings if w[0] == key[0]]
            result += sorted(temp, key=lambda val: val[0])[0][1] + ' '
        else:
            result += key + ' '
    return result


@app.route('/')
def home():
    return render_template('homepage.html', key="")

@app.route('/search',methods = ['Get'])
def searchResult():

    keyword = request.args.get("keyword")
    a, b, c, d, e, f = fetchResult(keyword)
    textSuggestion = ""
    if len(a) == 0 and len(b) == 0 and len(c) == 0:
        textSuggestion = doYouMean(keyword)
    return render_template('homepage.html', key=keyword, res_l1=a, res_l2=b, res_l3=c, imgres_l1=d, imgres_l2=e, imgres_l3=f, textSuggest=textSuggestion)

if __name__ == '__main__':
    app.run()
