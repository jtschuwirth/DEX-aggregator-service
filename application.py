
from flask import Flask, request
from flask_cors import CORS
from web3 import Web3
import json

app = Flask(__name__)
CORS(app)

main_net = 'https://rpc.s0.t.hmny.io'
w3 = Web3(Web3.HTTPProvider(main_net))

Tokens = json.load(open("data/tokens.json"))
Dexs = json.load(open("data/dexs.json"))
RouterABI = json.load(open("data/UniswapV2Router02.json"))

def getInputSwaps(inputToken, inputAmount, outputToken):
    result = []
    inAddress = Tokens[inputToken]["address"]
    inAmount = int(inputAmount * 10**Tokens[inputToken]["decimals"])
    outAddress = Tokens[outputToken]["address"]
    for router in Dexs:
        RouterContract = w3.eth.contract(address=Dexs[router]["address"], abi=RouterABI)
        if inAddress == Dexs[router]["main_token_address"] or outAddress == Dexs[router]["main_token_address"]:
             price = RouterContract.functions.getAmountsOut(inAmount, [inAddress, outAddress]).call()[1]
        else:
            price = RouterContract.functions.getAmountsOut(inAmount, [inAddress, Dexs[router]["main_token_address"], outAddress]).call()[2]
        price = price/(10**Tokens[outputToken]["decimals"])
        result.append({router: {inputToken: inputAmount, outputToken: price}})
    return result


@app.route("/", methods=['GET'])
async def getStatus():
    return {"Success": "API Working"}

@app.route("/tokens", methods=['GET'])
async def getTokens():
    result = []
    for token in Tokens:
        result.append(token)
    return {"result": result}

@app.route("/dexs", methods=['GET'])
async def getDexs():
    result = []
    for dex in Dexs:
        result.append(dex)
    return {"result": result}

@app.route("/swap/input", methods=['GET'])
async def getInputSwap():
    inputToken = request.args.get("inputToken", type = str)
    inputAmount = request.args.get("inputAmount", type = float)
    outputToken = request.args.get("outputToken", type = str)
    return {"result": getInputSwaps(inputToken, inputAmount, outputToken)}

app.run(host='0.0.0.0')