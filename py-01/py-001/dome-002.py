i=1#赋值给i
while(i<=100):#添加条件i<=100
    print(i)#
    i=i*2+1#将i取1执行运算逻辑

#a=[98,12,3,43,0,24,53,1,23,3,45]
#for i in range（len(a)-1,0-1)
#for




#无赋值，无返回值
def aa():#定义方法
    a=1
    b=3
    print(a+b)
aa()#执行方法
#有赋值，没有返回值
def bb(a,b):#将3赋值给a，9赋值给b
    print(a*b)
bb(3,9)
#无赋值，有返回值
def aa():#定义方法
    a=1
    b=3
    return a+b
c=aa()
print(c)
#执行方法
#有赋值，有返回值
def bb(a,b):#将3赋值给a，9赋值给b
    return a*b
c=bb(3,9)
print(c)