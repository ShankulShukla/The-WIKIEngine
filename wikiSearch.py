import _pickle as cPickle
import re
from nltk.stem import SnowballStemmer

def createResult(keyword, imageSearch = False, unigramSearch= False):

    if imageSearch:
        with open('imgind.txt', 'rb') as inp:
            index = cPickle.load(inp)

    else:
        with open('ind.txt', 'rb') as inp:
            index = cPickle.load(inp)

    # Pre-process search keyword
    keyword = re.sub('[\W\d]+', ' ', keyword).lower()
    st = SnowballStemmer('english')
    res_l1 = {}
    res_l2 = {}
    res_l3 = {}
    search_terms = keyword.split()
    stem_search_terms = [st.stem(key) for key in keyword.split()]
    for key, value in index.items():
        if keyword in key or key in keyword:
            res_l1[key] = value
        elif len(search_terms) == 1:
            temp_stem = st.stem(stem_search_terms[0])
            if temp_stem in key or key in temp_stem:
                res_l1[key] = value

    # multiple keyword search
    if len(search_terms) > 1:
        # diagram search
        diagram = [[search_terms[i], search_terms[i+1]] for i in range(len(search_terms)-1)]
        diagram_stem = [[stem_search_terms[i], stem_search_terms[i+1]] for i in range(len(stem_search_terms)-1)]
        for key, value in index.items():
            for i, ind in enumerate(diagram):
                dia = ind[0]+' '+ind[1]
                if (dia in key or key in dia) and (len(search_terms) > 2):
                    res_l2[key] = value
                else:
                    temp_stem = diagram_stem[i][0] + ' ' + diagram_stem[i][1]
                    if temp_stem in key or key in temp_stem:
                        res_l2[key] = value

    # if requested for extensive search
    if unigramSearch:
        for key, value in index.items():
            for i, ind in enumerate(search_terms):
                if ind in key or key in ind:
                    res_l3[key] = value
                else:
                    temp_stem = stem_search_terms[i]
                    if temp_stem in key or key in temp_stem:
                        res_l3[key] = value

    return res_l1, res_l2, res_l3

def fetchResult(keyword):

    res_l1, res_l2, res_l3 = createResult(keyword)
    imgres_l1, imgres_l2, imgres_l3 = createResult(keyword, imageSearch=True)

    return res_l1, res_l2, res_l3, imgres_l1, imgres_l2, imgres_l3
