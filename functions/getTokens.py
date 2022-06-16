import json

Tokens = json.load(open("constants/tokens.json"))

def getTokens():
    result = []
    for token in Tokens:
        result.append(token)
    return result