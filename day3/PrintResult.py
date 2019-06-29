print('---------------------------I LOVE JAVA--------------------------')


continueState = True
while continueState :
    isCon = True
    #成绩输入判断
    resultStr = input("考了多少分:")
    result = int(resultStr)
    if 100 > result >= 90 :
        print("A")
    elif 90 > result >= 80 :
        print("B")
    elif 80 > result >= 60 :
        print("C")
    elif 60 > result >= 0 :
        print("D")
    else :
        print("你是个神仙吧!过来挨打!WDNMD")
    while isCon :
        isContinue = input("还要继续吗?(Y/N)")
        if isContinue == "Y" :
            isCon = False
        elif isContinue == "N" :
            isCon = False
            continueState = False
        else :
            print("键入错误")
            
print("程序结束，拜拜了您内!")
    
    
