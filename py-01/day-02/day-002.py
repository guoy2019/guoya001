#for i in range(1,100):
#    print(i)


def ss():
    for i in range(1,10):
        for j in range(1,i+1):
            print(i,"x",j,"=",i*j,"\t",end="")#\t制表符,end是隔行
        print()
ss()


#def aa(a,b=12):#默认b=12
 #   return a+b
#print(aa(12))#默认把12赋值给a，b=12
#print(aa(23,56))#把23赋值给a，12赋值给b
#print(aa(a=45,b=45))#把45赋值给a，45赋值给b


#def bb(*args,**kwargs):
 #   print(args)
  #  print(kwargs)
