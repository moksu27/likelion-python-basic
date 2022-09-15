import random

num= int(input("구매할 로또 개수 : "))

for i in range(num):
    randomNumber = random.sample(range(1,46),6)
    randomNumber.sort()
    print(randomNumber)
