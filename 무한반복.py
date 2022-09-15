#무한반복
while 10 < 90 :
    print("True")
    a=input("esc=q : ")
    if  a == 'q':
        break

#순차출력
i = 5

while i >= 0 :
    print(i)
    i = i - 1

#브레이크문
i = 0
while True :
    print(i)
    i = i + 1

    if i >= 3 :
        print("if문 동작")
        break

print("반복문 종료!")
 
#건너뛰기
i = 0
while i < 10 :
    i = i + 1

    if i % 2 == 0 :
        continue
    print(i)

print("반복 종료!")


#범위지정
for x in range(10, 20) : 
    print(x)

#x부터 y까지 z만큼
for y in range(3, 31, 3) :
    print(y)


result = 0

# 1부터100까지의 합
for x in range(1, 101) :
    result = result + x

print(result)

# 1부터 10까지의 곱
for x in range(1, 11) :
    result = result * x

print(result)