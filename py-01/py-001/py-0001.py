#print("nihao")
#基础变量类型：小数，数字，字符串，
#等号为赋值，右边为数字，左边为变量名
"""
变量特性：
先创建后使用
变量名在同一作用域中唯一一个变量只能存在一个值
变量中存的值是最新的
变量名要求：
不能使用Python关键字
只能包含英文，数字，下划线，且数字不能开头
命名规范：
包名全小写，多个单词中间用下划线链接
类名每个单词首字母大写TestDemo
方法名全小写，多个单词中间用下划线链接
变量名全小写，多个单词中间用下划线链接

"""
#a=1
#type为方法名
#print(type(a))
#print(a)
#b=1.1#小数类型
#print(b)
#print(type(b))
#c="1"#字符串类型
#print(c)
#print(type(c))
#d='1'
#print(d)
#print(type(d))
#d1='''1'''
#print(d1)
#print(type(d1))
#d11="""1"""
#print(d11)
#print(type(d11))
#容器类型：列表，元组，字典

#e=[1,1.2,23,43.]
#print(e)#列表

#print(type(e))
#f=(1,)#元组，，，，单个数字用逗号结尾，多个数字用逗号隔开
#print(f)
#print(type(f))
h={"nihao":"nishi","nizainali":"nishishui"}#字典成对出现
print(h)
print(type(h))


# 冒泡排序
a = [90,43,2,63,6,3,4]
for i in range(len(a)-1,0,-1):#len(a)-1表示根据下标确定最后一位的 0为边界，开区间表示下标为“1”即确定第二个数，-1表示倒序排列
    for j in range(i):#
        if(a[j] >a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
print(a)

a = [90,43,2,63,6,3,4]
for i in range(len(a)-1,0,-1):#len(a)-1表示根据下标确定最后一位的 0为边界，开区间表示下标为“1”即确定第二个数，-1表示倒序排列
    for j in range(i):#
        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
print(a)


