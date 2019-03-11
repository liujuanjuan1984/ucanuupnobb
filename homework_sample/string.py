import random

"""
String的各种骚操作：

https://docs.python.org/3/tutorial/inputoutput.html

"""

#字符串的赋值与操作
astr = 'Python'
bstr = "    "
cstr = '\n'
dstr = astr + 'Good Job!' 
estr = 'LiuJuanjuan'
fstr = astr + bstr * 2 + cstr * 3 + dstr * 2 + estr


#打印字符串，同时输出该字符串的长度（有多少个字符）
print('astr的值是：',astr,len(astr))
print('bstr的值是：',bstr,len(bstr))
print('cstr的值是：',cstr,len(cstr))
print('dstr的值是：',dstr,len(dstr))
print('estr的值是：',estr,len(estr))
print('fstr的值是：',fstr,len(fstr))

#遍历字符串：
print('开始演示遍历字符串\n\n')
for i in astr:
    print(i,astr.index(i))

print('开始演示遍历字符串，并做替换\n\n')
for j in dstr:
    dstr.replace(j,'d')
    print(dstr,j)
print(dstr,"还是原来的它吗？\n是的，dstr没有改变。\n\n")

print('再次演示替换，但我们采用了赋值')
for j in dstr:
    dstr = dstr.replace(j,'×')
    print(dstr,j)
print(dstr,"还是原来的它吗？\n不是，dstr被改变了。\n\n")


#字符串替换：
print('开始演示字符串替换\n\n')
print('dstr的初始值是：',dstr)
print('estr的初始值是：',estr)
dstr = estr
print('经过 dstr = estr后,dstr是：', dstr)
print('经过 dstr = estr后,dstr是：', estr)

#检索字符串
afind = estr.find('ua') #仅返回最近一次的，并不会返回所有
acount = estr.count('u')
acount = estr.count('U')
aindex = estr.index('u') #并不算常规方法？
aupper = estr.upper()
alower = estr.lower()

print(afind,'发现\'u\'的位置')
print(acount,'发现\'u\'的次数')
print(aindex,'发现\'u\'的位置')
print(aupper,'字符串全部大写')
print(alower,'字符串全部小写')



#字符串的“切片”
print('开始演示字符串的切片\n\n')
print('estr的初始值是：',estr)
print('estr[:]的值是：',estr[:]) #为了避免影响原字符串，有时候会采用切片的方式来拷贝一个新的字符串？
print('estr[0:2]的值是：',estr[0:2])#[]的规律是：左包括，右不包括
print('estr[:2]的值是：',estr[:2])
print('estr[2:4]的值是：',estr[2:4])
print('estr[-4:-1]的值是：',estr[-4:-1])#倒数第四位，到倒数第一位但不包括倒数第一位


#字符串切片的应用，其实我的感受还不深，只是知道可以这么玩儿。
for x in estr[:]:
    estr[:].replace(x,'√')
    print(estr)
    print(estr[:]) #无论是否切片，目前这种方式都不会改变字符串。

#操作列表导致列表被改变而带来的问题，可以查看list.py


#尚未不了解的方法还有很多……

#往字符串指定位置插入新的字符串



