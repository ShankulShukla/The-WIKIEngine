import json
import os
def update(new_index):
    #This function can be used to extend the index of the search and increase scope of the search serving
    if os.path.isfile("ind.json") == False: # if file do-not exist
        with open('ind.json','w') as op:
            json.dump(new_index,op)
        return

    with open('ind.json','r') as inp:
        old_index=json.load(inp)

    #union of the new with the old dictionary
    for i in new_index.keys():
        if i in old_index.keys():
            for j in new_index[i]:
                old_index[i].append(j)
        else:
            old_index[i]=new_index[i]

    with open('ind.json', 'w') as op:
        json.dump(new_index,op)

