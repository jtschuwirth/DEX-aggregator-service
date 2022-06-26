import json

Blockchains = json.load(open("constants/blockchains.json"))

def getBlockchains():
    result = []
    for blockchain in Blockchains:
        result.append(blockchain)
    return result