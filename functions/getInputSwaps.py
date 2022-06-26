from web3 import Web3
from pycoingecko import CoinGeckoAPI
import json

cg = CoinGeckoAPI()

Tokens = json.load(open("constants/tokens.json"))
Dexs = json.load(open("constants/dexs.json"))
RouterABI = json.load(open("constants/UniswapV2Router02.json"))
FactoryABI = json.load(open("constants/UniswapFactory.json"))
Blockchains = json.load(open("constants/blockchains.json"))

def pathEvaluation(price, oracle_price):
    if price > oracle_price*1.5 or price < oracle_price*0.5:
        return False
    else:
        return True

def getOraclePrice(inputToken, outputToken, inAmount):
    input_id=Tokens[inputToken]["cgId"]
    output_id=Tokens[outputToken]["cgId"]
    input_price = cg.get_price(ids=input_id, vs_currencies='usd')
    output_price = cg.get_price(ids=output_id, vs_currencies='usd')
    input_price = input_price[input_id]["usd"]
    output_price = output_price[output_id]["usd"]
    return (input_price/output_price)*inAmount

def getPrice(RouterContract, inputToken, outputToken, inputAmount, blockchain):
    inputAmount = int(inputAmount)
    inAddress = Tokens[inputToken][blockchain]
    outAddress = Tokens[outputToken][blockchain]
    if len(inAddress) == 0 or len(outAddress) == 0:
        return 0 
    inAmount = int(inputAmount * 10**Tokens[inputToken]["decimals"])
    oracle_price = getOraclePrice(inputToken, outputToken, inputAmount)
    try:
        price = RouterContract.functions.getAmountsOut(inAmount, [inAddress, outAddress]).call()[1]
        price = price/(10**Tokens[outputToken]["decimals"])
        valid = pathEvaluation(price, oracle_price)
        if valid:
            #print("Direct Path:", inputToken, outputToken)
            return price
    except:
        pass
    for token in Tokens:
        if token == inputToken or token==outputToken:
            continue
        try:
            price = RouterContract.functions.getAmountsOut(inAmount, [inAddress, Tokens[token]["address"], outAddress]).call()[2]
            price = price/(10**Tokens[outputToken]["decimals"])
            valid = pathEvaluation(price, oracle_price)
            if valid:
                #print("Complexity 1 Path:", inputToken, token,outputToken)
                return price
        except:
            continue
    return 0
    


def getInputSwaps(inputToken, inputAmount, outputToken, blockchain):
    w3 = Web3(Web3.HTTPProvider(Blockchains[blockchain]))
    result = []
    for dex in Dexs:
        if len(Dexs[dex][blockchain]) == 0:
            continue
        RouterContract = w3.eth.contract(address=Dexs[dex][blockchain], abi=RouterABI)
        price = getPrice(RouterContract, inputToken, outputToken, inputAmount, blockchain)
        if price == 0:
            result.append({dex: "Can't find a valid path"})
        else:
            result.append({dex: {"input": {"name": inputToken, "amount": inputAmount}, "output": {"name": outputToken, "amount": price}}})
    return result
