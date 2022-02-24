from abc import get_cache_token
from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scipts import deploy_mocks, get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONEMETS
from web3 import Web3

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONEMETS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else: 
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks Deployed")

    fund_me = FundMe.deploy(price_feed_address,{"from":account}, publish_source = config["networks"][network.show_active()].get("verify"))
    print(f"Contract depoyed to {fund_me.address}")
    return fund_me
    print(network.show_active())


def main():
    deploy_fund_me()