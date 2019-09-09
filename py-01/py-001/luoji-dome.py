#if逻辑运算语句
a=1#把1赋给a
if(a==0):#如果a为0，不符合条件，则执行else条件
    print("买个桃子")#打印输出“买个桃子”
else:#如果
    print("买个西瓜")

s=75
if(s>=80):
    print("优秀")
if(s<=80 and s>=60):
    print("良好")
if(s<=60):
    print("不及格")



s=75
if(s>=80):
    print("优秀")
elif(s>=60):
    print("良好")
elif(s<=60):
    print("不及格")