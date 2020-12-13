import tda
from tda import auth,client
from tda.orders.equities import equity_buy_limit,equity_sell_limit,equity_buy_market,equity_sell_market
import requests

#-----------config------------
api_key=''
token_path=r""
redirect_uri=''
chromedriver_path=r""
account_id=''
#-----------config------------

#Buy
def BUY_LIMIT(symbol,quantity,price):
    Client=GET_AUTH()
    limit_buy=tda.orders.equities.equity_buy_limit(symbol,quantity,price)
    Client.place_order(account_id, limit_buy)
def BUY_MARKET(symbol,quantity):
    Client=GET_AUTH()
    market_buy=tda.orders.equities.equity_buy_market(symbol,quantity)
    Client.place_order(account_id, market_buy)
#Sell
def SELL_LIMIT(symbol,quantity,price):
    Client=GET_AUTH()
    limit_sell=tda.orders.equities.equity_sell_limit(symbol,quantity,price)
    Client.place_order(account_id, limit_sell)
def SELL_MARKET(symbol,quantity):
    Client=GET_AUTH()
    market_sell=tda.orders.equities.equity_sell_market(symbol,quantity)
    Client.place_order(account_id, market_sell)

#Quote
def GET_QUOTE(symbol):
    url='https://api.tdameritrade.com/v1/marketdata/{0}/quotes?apikey={1}'.format(symbol,api_key)
    re=requests.get(url)
    data=re.json()
    return data[symbol]


#Auth
def GET_AUTH():
    try:
        client=auth.client_from_token_file(token_path, api_key)
        return client
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome(executable_path=chromedriver_path) as driver:
            client = auth.client_from_login_flow(
                driver, api_key, redirect_uri, token_path)
            return client

