import copy

def dict(indict, amount=9):

    counter = 0
    tempdict = {}
    result = []
    addlast = False

    for a, b in indict.items():

        if counter < amount:

            tempdict[a]=b
            counter += 1
            addlast = True
        else:

            result.append(copy.deepcopy(tempdict))
            tempdict = {}
            counter = 1
            tempdict[a]=b

    result.append(copy.deepcopy(tempdict))
    return result
