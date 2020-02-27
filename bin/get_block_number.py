from web3 import Web3
import web3
import logging
import os
import requests


infura_token = "59d7fd40b0b94a9a9ce4dcab99c1f0"
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{token}"))

print(w3.eth.blockNumber)
