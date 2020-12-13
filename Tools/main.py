import API.Tool as T
from datetime import datetime
import time

with open('DATA/FB_12-8.txt','w') as f:
    while (datetime.now().strftime("%H")!="04"):
        for i in range(5):
            value=T.GET_QUOTE('FB')
            f.write(str(value)+'\n')
            print(value)
            time.sleep(30)