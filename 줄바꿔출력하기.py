a = int(input("숫자 : "))

for x in range (1, a+1):
    if x % 10 == 0:
        print()
    else:
        print(x+1, end=" ")