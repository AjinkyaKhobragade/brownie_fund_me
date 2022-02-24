from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3
DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONEMETS = ["development","ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONEMETS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_keys"])

def deploy_mocks():
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE, {"from": get_account()} )
            print("Mock Deployed!")