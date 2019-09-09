class ClassDome_pp():#类名
    def aa(self):#创建aa方法   self代表自己本身
        print("我是马冬梅")
    def bb(self):#创建bb方法
        print("我是夏洛")
        self.aa()#调用aa的方法
if __name__ == '__main__':#使用main方法
    c=ClassDome_pp()#将类名ClassDome赋值给c
    c.aa()#执行aa方法
    c.bb()#执行bb方法



g="dergakio"#dergakio   要求生成两个新的字符串  drai  和egko
print(g[::2])#下标从0开始，到结尾 步长为2
print(g[1::2])

c="hvshijshdhci9jnihijidhbhcuhiunhihihckjfoj"
print(c[::])
print(c[3:7:2])
print(c[::-1])#倒序排列
print(c+c+c)#拼接字符串=print（c*3）

r="ko,ijfin,icdjhivn,jvifjnv,jvijnvim,cuhf"
print(r.split("i"))#字符串切片，（用字符串中有的元素切割）
s= "   iosjive joiejgvo ijvoedmvled oivoe        "
print(s.strip())#去掉前后空格
print(s.lstrip())#去掉右边空格
print(s.rstrip())#去掉左边空格
print(s.replace(" ", ""))#去掉全部空格

t="kvmijgpijboiejbi    kvpoekjvpojp'''''''''"""""""
print(t.replace('"',"'"))#替换
print(len(t))



y="GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
#print(y[0:4])#请求方法
print(y.split(" "))
print(y.[0])
#print
