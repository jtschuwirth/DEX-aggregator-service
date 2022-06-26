import json

Tokens = json.load(open("constants/tokens.json"))

def getTokens(blockchain):
    result = []
    for token in Tokens:
        if len(Tokens[token][blockchain]) != 0:
            result.append(token)
    return result