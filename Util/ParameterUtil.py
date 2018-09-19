import random
from datetime import datetime

#리스트에 있는 랜덤 값 str으로
def getRandomData(arr,num):
    res = ""
    for i in range(num,0,-1):
        idx = random.randrange(0,len(arr))
        res = res + arr.pop(idx) + " "
    return res


#정수형 month -> string 컨버터
def ConvertMonthParameter(mon):
    print('mon : ' + str(mon))
    ret = ''
    if(mon == '이달의'):
        ret = str(datetime.today().month)
    else:
        ret = mon
    if(len(ret)==1):
        ret = "0" + ret
    print('converted mon : ' + ret)
    return ret


#정수형 month -> 글자형 str
def ConvertMonthToStr(mon):
    print('ConvertMonthToStr - mon : ' + str(mon))
    ret = ''
    if(mon == '이달의'):
        ret = str(datetime.today().month)
    else:
        ret = mon
    if(ret == '1'):
        ret = '일월'
    elif(ret == '2') :
        ret = '이월'
    elif (ret == '3'):
        ret = '삼월'
    elif (ret == '4'):
        ret = '사월'
    elif (ret == '5'):
        ret = '오월'
    elif (ret == '6'):
        ret = '육월'
    elif (ret == '7'):
        ret = '칠월'
    elif (ret == '8'):
        ret = '팔월'
    elif (ret == '9'):
        ret = '구월'
    elif (ret == '10'):
        ret = '시월'
    elif (ret == '11'):
        ret = '십일월'
    else : 
        ret = '십이월'
    print('ConvertMonthToStr - converted mon : ' + ret)
    return ret