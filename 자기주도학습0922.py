#파이썬 기초
'''
import random

def 가위바위보 (me):
    computer=random.randint(1,3)
    if me == computer:
        print("비겼습니다")

    if me == 1:
        if computer == 2:
            print("졌습니다")
        elif computer == 3:
            print("이겼습니다")
    
    if me == 2:
        if computer == 1:
            print("이겼습니다")
        elif computer == 3:
            print("졌습니다")
    
    if me == 3:
        if computer ==2:
            print("이겼습니다")
        elif computer == 1:
            print("졌습니다")


me=[]
num = int(input("진행할 횟수를 입력하세요: "))
for i in range(num):
    me.append(input(f"{num}번 가위, 바위, 보를 입력하세요: "))
    if me[i] == '가위':
        me[i] = 1
    elif me[i] == '바위':
        me[i] = 2
    elif me[i] == '보':
        me[i] = 3

for i in range(num):
    가위바위보(me[i])
'''

#판다스를 이용한 데이터 프레임
import pandas as pd
import numpy as np

#데이터 프레임 생성
df = pd.DataFrame({
    '날짜':pd.date_range(start='20220914', end = '20220922').astype('str'),
    '요일':['월','화','수','목','금','토','일','월','화'],
    '지출내역': np.random.randint(0,10000,9),
    '비고':['멋사시작',np.nan,np.nan,np.nan,'파이썬',np.nan,np.nan,'seaborn','인싸']})

df.info()
df.shape
df.dtypes
df.describe()
print(df['날짜'])