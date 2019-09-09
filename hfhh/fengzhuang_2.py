

class ClassDome_qqq():#2.申明一个类名为classdome_qqq
    def aaa(self):#1.申明一个方法为aaa
        print("我是爷爷")#print“aaa”

    def bbb(self):
        print("我是爸爸")

    def ccc(self):
        print("我是儿子")


classmethod_1=ClassDome_qqq()#3将类名ClassDome实例化为classmethod_1
classmethod_1.aaa()#通过实例化classmethod_1调用aaa的方法
classmethod_1.bbb()#通过实例化classmethod_1调用bbb的方法
classmethod_1.ccc()#通过实例化classmethod_1调用ccc的方法

class ClassDome_mm():#类名
    def aa1(self):#创建aa方法   self代表自己本身
        print("我是马冬梅")
    def bb1(self):#创建bb方法
        print("我是夏洛")
        self.aa1()#调用aa的方法

classmethod_2=ClassDome_mm()#将类名ClassDome赋值给c
classmethod_2.aa1()#执行aa方法
classmethod_2.bb1()#执行bb方法