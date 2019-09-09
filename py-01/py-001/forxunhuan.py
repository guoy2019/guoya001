#for i in range(1,100,2):
#    print(i)

#a=range(1,100,2)

#print(a%2)





"""for i in range(100):
    if (i==10):
        break
    print(i)


for i in range(100):
    if(i%10==1):
        continue
    print(i)
# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)


s = 0
for i in range(1,101):
    s += i
print(s)"""






# 求出100以内的质数

for i in range(2,100):
    f = False # 标记i是否被整除
    for j in range(2,i):
        if(i%j==0):
            f = True #如果i被整除，把f值改成True
            break
    if (not f):
        print(i)

# 打印出九九乘法表（循环嵌套）
for i in range(1,10):#for循环且i的取值范围1-9不包含末尾最后一位
    for j in range(1,i+1):#for循环且i的取值范围1-i不包含末尾最后一位
        print(j,"X",i,'=',i*j,'\t',end='')#\t制表符，end将乘的运算分行
    print()

    # 求出1+2+3.。。+100和
    s = 0
    for i in range(1, 101):
        s += i
    print(s)


# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)


for i in range(1,10):
    for j in range(1,1+i):
        print(j,'x',i,'=',i*j, end='' "\t")
    print()
for i in range(1,10):
    for j in range(1,1+i):
        print(i,"x",j,"=",i*j,"\t",end="")
    print()