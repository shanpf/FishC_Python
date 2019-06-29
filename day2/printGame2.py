import random

print('---------------------------I LOVE JAVA--------------------------')

secert = random.randint(1,10)
i = 0

while i<3 :
    
    i = i+1
    
    temp = input("猜猜数字:")

    guess = int(temp)
                
    if guess == secert:
                    
        print("牛批")
        print("但没什么卵用")
        break
    else:
                    
        if guess > secert:
                        
            print("大了你猜错的样子像CXK")
        else:
                        
            print("小了你猜错的样子像CXK")
        #print("嘻嘻，你猜错的样子像CXK")

            
print("游戏结束，不玩啦")
