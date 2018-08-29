import random

#리스트에 있는 랜덤 값 str으로
def getRandomIDataInArray(arr,num):
    res = ""
    for i in range(num,0,-1):
        idx = random.randrange(0,i)
        res = res + arr.pop(idx) + " "
    return res

#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    print(getRandomIDataInArray(["123","456","1123"],2))

