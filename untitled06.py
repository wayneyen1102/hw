import random
for i in range(5):
    y = random.randint(1,20)
    x = input('輸入1到20其中一個數字')
    x = int(x)
    if x == y:
        print('答對')
    elif x > y:
        print('太大')
    elif x < y:
        print('太小')
while x == y:
        break

    
    
    

    
