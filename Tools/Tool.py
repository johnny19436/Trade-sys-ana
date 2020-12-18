import tda
from tda import auth,client
from tda.orders.equities import equity_buy_limit,equity_sell_limit,equity_buy_market,equity_sell_market
import requests
import pandas as pd
import csv

#-----------config------------
api_key='QOADHYNDDJVOI3JY4WCOBCNYSGOHAWZN@AMER.OAUTHAP'
token_path=r""
redirect_uri=''
chromedriver_path=r""
account_id=''
#-----------config------------

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

#Cleaning data
def CLEAN_DATA(from_dir,to_dir):
    df=pd.read_csv(from_dir)
    df=df.dropna()
    df.drop(['Open','High','Low','Close'],axis=1,inplace=True)
    df.rename(columns={'Adj Close': 'Close'}, inplace=True)
    df.to_csv(to_dir)

#-------------Indicators----------------
def RSI(from_dir,to_dir,N):
    df=pd.read_csv(from_dir)

    a=[]
    a.append(0)
    for i in range(1,df.shape[0]):
        k=df.loc[i]['Close']-df.loc[i-1]['Close']
        a.append(k)

    with open(to_dir,'w',newline='') as f:
        thewriter=csv.writer(f)
        thewriter.writerow(['idx','RSI'])
        for i in range(N,df.shape[0]):
            up = 0
            dn = 0
            for k in range(i-N+1,i+1):
                p = a[k]
                if p > 0:
                    up+=p
                else:
                    dn+=p
            RSI=round(up/(up-dn)*100, 2)
            thewriter.writerow([i,RSI])
    df=pd.read_csv(to_dir)
    df.set_index("idx" , inplace=True)
    df.to_csv(to_dir)
