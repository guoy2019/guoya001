#def aa(a,b):#申明一个方法为“aa”
 #   try:#尝试执行c=a/b
  #      c = a / b
   # except:#如果上面出问题就执行下面步骤
    #    print("ss")
     #   return
    #return c  #函数得到一个返回值“c”
#print(aa(11,2)) #调用aa的方法

def aa(a,b):
    try:
        c=a*b
    except:
        print("vv")
        return
    return c
print(aa(23,0))
