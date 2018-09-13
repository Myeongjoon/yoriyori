import random
from datetime import datetime

#리스트에 있는 랜덤 값 str으로
def getRandomData(arr,num):
    res = ""
    for i in range(num,0,-1):
        idx = random.randrange(0,i)
        res = res + arr.pop(idx) + " "
    return res


#정수형 month -> string 컨버터
def ConvertMonthParameter(mon):
    print('mon : ' + mon)
    ret = ''
    if(mon == '이달의'):
        ret = str(datetime.today().month)
    if(len(mon)==1):
        ret = "0"+ mon
    print('converted mon : ' + ret)
    return ret