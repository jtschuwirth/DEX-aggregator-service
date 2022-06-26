import json

Dexs = json.load(open("constants/dexs.json"))

def getDexes(blockchain):
    result = []
    for dex in Dexs:
        if len(Dexs[dex][blockchain]) != 0:
            result.append(dex)
    return result