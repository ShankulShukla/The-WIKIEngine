import _pickle as cPickle
import os


def update(new_index, new_imgIndex):
    #This function can be used to extend the index of the search and increase scope of the search serving
    if os.path.isfile("ind.txt") == False: # if file do-not exist
        with open('ind.txt','wb') as op:
            cPickle.dump(new_index,op)
    else:
        with open('ind.txt','rb') as inp:
            old_index = cPickle.load(inp)

        #union of the new with the old dictionary
        for i in new_index.keys():
            if i in old_index.keys():
                for j in new_index[i]:
                    old_index[i].add(j)
            else:
                old_index[i]= new_index[i]

        with open('ind.txt', 'wb') as op:
            cPickle.dump(old_index,op)

    if os.path.isfile("imgind.txt") == False:  # if file do-not exist
        with open('imgind.txt', 'wb') as op:
            cPickle.dump(new_imgIndex, op)
    else:
        with open('imgind.txt', 'rb') as inp:
            old_index = cPickle.load(inp)

        # union of the new with the old dictionary
        for i in new_imgIndex.keys():
            if i in old_index.keys():
                for j in new_imgIndex[i]:
                    old_index[i].add(j)
            else:
                old_index[i] = new_imgIndex[i]

        with open('imgind.txt', 'wb') as op:
            cPickle.dump(old_index, op)