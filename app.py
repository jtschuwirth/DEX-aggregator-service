from functions.getInputSwaps import getInputSwaps
from functions.getTokens import getTokens
from functions.getDexes import getDexes

def handler(event, context):
    if event["method"] == "getInputSwaps":
        return {"results": getInputSwaps(event["inputToken"], event["inputAmount"], event["outputToken"], event["blockchain"])}
    elif event["method"] == "getTokens":
        return {"tokens": getTokens(event["blockchain"])}
    elif event["method"] == "getDexes":
        return {"dexes": getDexes(event["blockchain"])}
