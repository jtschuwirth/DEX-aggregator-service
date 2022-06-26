from functions.getInputSwaps import getInputSwaps
from functions.getTokens import getTokens
from functions.getDexes import getDexes
from functions.getBlockchains import getBlockchains

print(getBlockchains())
print(getTokens("polygon"))
print(getDexes("polygon"))
print(getInputSwaps("matic", 1, "btc", "polygon"))