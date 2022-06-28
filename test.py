from functions.getSwaps import getInputSwaps, getOutputSwaps
from functions.getTokens import getTokens
from functions.getDexes import getDexes
from functions.getBlockchains import getBlockchains

print(getBlockchains())
print(getTokens("polygon"))
print(getDexes("polygon"))
print(getInputSwaps("matic", 1, "btc", "polygon"))
print(getOutputSwaps("matic", 1, "eth", "polygon"))

def test_getBlockchains():
    assert isinstance(getBlockchains(), list)

def test_getTokens():
    assert isinstance(getTokens("polygon"), list)
    assert isinstance(getTokens("harmony"), list)

def test_getDexes():
    assert isinstance(getDexes("polygon"), list)
    assert isinstance(getDexes("harmony"), list)

def test_getInputSwaps():
    assert isinstance(getInputSwaps("matic", 1, "btc", "polygon"), list)

def test_getOutputSwaps():
    assert isinstance(getOutputSwaps("matic", 1, "btc", "polygon"), list)


