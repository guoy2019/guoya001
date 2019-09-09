#字典新增
a={}
a={"name":"xioaming","school":"wh"}#创建一个字典
print(a)
a["sex"]="nv"#新增一条信息

a["aa"]="23"
print(a)

#print(a.pop("school"))#删除key值shool
#print(a)
#del a["sex"]删除key值为sex（只能对key进行操作）
#print(a)

#del a全删字典
#print(a)

#a.clear()#清空数据
#print(a)

#a ["name"]="小明"
#print(a)


#3print(len(a))

aa={"1":"23","2":"989"}
a.update(aa)
print(a)

print(dict(a,**aa))
