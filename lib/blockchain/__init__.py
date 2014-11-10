'''
Proxy API to make queries to popular blockchains explorer
'''
import sys

from lib import config
import blockr, insight, sochain, jmcorgan

# http://test.insight.is/api/sync
def check():
    return sys.modules['lib.blockchain.{}'.format(config.BLOCKCHAIN_SERVICE_NAME)].check()

# http://test.insight.is/api/status?q=getInfo
def getinfo():
    return sys.modules['lib.blockchain.{}'.format(config.BLOCKCHAIN_SERVICE_NAME)].getinfo()

# example: http://test.insight.is/api/addr/mmvP3mTe53qxHdPqXEvdu8WdC7GfQ2vmx5/utxo
def listunspent(address):
    return sys.modules['lib.blockchain.{}'.format(config.BLOCKCHAIN_SERVICE_NAME)].listunspent(address)

# example: http://test.insight.is/api/addr/mmvP3mTe53qxHdPqXEvdu8WdC7GfQ2vmx5
def getaddressinfo(address):
    return sys.modules['lib.blockchain.{}'.format(config.BLOCKCHAIN_SERVICE_NAME)].getaddressinfo(address)

# example: http://test.insight.is/api/tx/c6b5368c5a256141894972fbd02377b3894aa0df7c35fab5e0eca90de064fdc1
def gettransaction(tx_hash):
    return sys.modules['lib.blockchain.{}'.format(config.BLOCKCHAIN_SERVICE_NAME)].gettransaction(tx_hash)

def get_pubkey_for_address(address):
    """attempts to get the public key from an address. the address must have at least made one transaction"""
    return sys.modules['lib.blockchain.{}'.format(config.BLOCKCHAIN_SERVICE_NAME)].get_pubkey_for_address(address)
