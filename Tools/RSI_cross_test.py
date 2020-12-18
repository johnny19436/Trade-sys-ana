import pandas as pd

rsi=pd.read_csv('C:/Users/johnn/OneDrive/桌面/repo/Data/Indicators/RSI/Nasdaq.csv')
df=pd.read_csv('C:/Users/johnn/OneDrive/桌面/repo/Data/Raw/c_Nasdaq.csv')
#DJI:70,85
#S&P500:75,80
#Nasdaq:(不佳)

N=9

for j in range(35,100,5):
    for k in range(90,j-10,-5):
        start=0
        end=0
        for i in range(0,N):
            start+=df.iloc[i]['Close']
        start/=N
        for i in range(df.shape[0]-N,df.shape[0]):
            end+=df.iloc[i]['Close']
        end/=N

        total=0
        p=0
        for i in range(0,rsi.shape[0]):
            if rsi.iloc[i]['RSI']<=j:
                total=df.iloc[i]['Close']
                start=total
                p=1
                break
        for i in range(9,df.shape[0]):
            if p==0 and rsi.iloc[i-N]['RSI']<=j:
                total-=df.iloc[i]['Close']
                p=1
            elif p==1 and rsi.iloc[i-N]['RSI']>=k:
                total+=df.iloc[i]['Close']
                p=0
        if p==1:
            total+=df.iloc[df.shape[0]-1]['Close']

        print(total/end)
    print("--------"+str(j)+"---------")