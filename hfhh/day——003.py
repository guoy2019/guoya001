#open打开文件，使用r可读，使用w可写，使用a追加
a=open("test.txt","r")#可读
print (a.readlines())#可读，显示在一行
print(a.read())#可读按行显示（分行）



#a=open("test.txt","w")
#a.writelines(["sjkvhshn","nvhshgv","kjhckjahfiol"])以字符串的格式显示，且加[]
#a.write("nvkjsnblk\nsgdn")#以字符串的格式显示，且加[]，\n表示换行
#a.close()