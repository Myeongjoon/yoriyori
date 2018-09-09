import random

#리스트에 있는 랜덤 값 str으로
def getRandomIDataInArray(arr,num):
    res = ""
    for i in range(num,0,-1):
        idx = random.randrange(0,i)
        res = res + arr.pop(idx) + " "
    return res