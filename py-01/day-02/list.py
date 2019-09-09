a=[1,2,3,6,5,4,6,9,8,7,9]
a.append(11)#在数组末尾新增数据用append
print(a)
a.insert(4,12)#在组数中间新增数据用insert
print(a)
b=[34,45,56]#新增一个列表，先申明一个列表b
a.extend(b)#新增一个列表用extend
print(a)


print(a.pop(3))#删除下标对应的数
print(a)
print(a.pop(-1))#删除倒数第一下标
print(a)


a.remove(3)#删除数字（用remove）
print(a)

a[1]=90
print(a)

a.index(4)
print(a.index())