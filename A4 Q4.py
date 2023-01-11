import random
while True:
    a = random.randint(0,200)
    if a%5==2 and a%6==3 and a%7==2:
        print(a)
        break
    else:
        continue 


