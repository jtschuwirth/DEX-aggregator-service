from functions.getInputSwaps import getInputSwaps
from functions.getTokens import getTokens
from functions.getDexes import getDexes

def handler(event, context):
    if event["method"] == "getInputSwaps":
        return {"results": getInputSwaps(event["inputToken"], event["inputAmount"], event["outputToken"])}
    elif event["method"] == "getTokens":
        return {"tokens": getTokens()}
    elif event["method"] == "getDexes":
        return {"dexes": getDexes()}
