import pandas as pd

rsi=pd.read_csv('C:/Users/johnn/OneDrive/桌面/repo/Data/Indicators/RSI/DJI.csv')
df=pd.read_csv('C:/Users/johnn/OneDrive/桌面/repo/Data/Raw/c_DJI.csv')

N=9

start=0
for i in range(0,N):
    start+=df.iloc[i]['Close']
start/=N

end=0
for i in range(df.shape[0]-N,df.shape[0]):
    end+=df.iloc[i]['Close']
end/=N

total=0
p=0

for i in range(0,rsi.shape[0]):
    if rsi.iloc[i]['RSI']<=90:
        total=df.iloc[i]['Close']
        start=total
        p=1
        break

for i in range(0,rsi.shape[0]):
    if p==0 and rsi.iloc[i]['RSI']<=90:
        total-=df.iloc[i+N]['Close']
        p=1
    elif p==1 and rsi.iloc[i]['RSI']>=90:
        total+=df.iloc[i+N]['Close']
        p=0
if p==1:
    total+=df.iloc[df.shape[0]-1]['Close']
print(total/start)

print(end/start)
print(total/end)
#print(total/end)

