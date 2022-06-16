import json

Dexs = json.load(open("constants/dexs.json"))

def getDexes():
    result = []
    for dex in Dexs:
        result.append(dex)
    return result