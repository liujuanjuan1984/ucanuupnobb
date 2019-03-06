"""
布尔值：True False 首字母必须大写。Python对大小写敏感。

布尔运算：
    一维：not
    二维：and or
二维运算从左到右执行，一维运算优先级高于二维。

布尔运算的返回结果是布尔值。

sample功能：因为挨个写公式，并通过print()来断点很麻烦（要重复写/粘贴很多次print())，所以干脆写了个列表来遍历。

初学者只需关心布尔运算的表达式的返回值是什么，而不必掌握该文件内的写法。虽然不必掌握，但其实你也可以读懂！

"""

#把布尔运算的所有表达式，写在列表中。
alist = [
    True, #True 1
    False, #False 2
    True == 1, #True 3
    True == 0, #False 4
    False == 0, #True 5
    False == 1, #False 6
    True and True, #True 7
    True and False, #False 8
    True or True, #True 9
    True or False, #True 10
    False and True, #False 11
    False and False, #False 12
    False or True, #True 13
    False or False, #False 14
    not True, #False 15
    not False, #True 16
    True and not True, #False 17
    False or not False, #True 18
    True and True or not False and True] #True 19

#通过for循环遍历列表，来检查每个表达式的输出值是什么。
i = 1
for a in alist[:]:
    if a == True :
        print(i,a,'is True.')
    else:
        print(i,a,'is false.')
    i += 1

"""
走过的弯路&未解决的疑问：

我期待通过遍历列表元素并打印的方式，来阐述计算结果。但：

print(str(a),'is True.')
print(a,'is True.')

无论上述哪个语句，
又或者把what表达式先转换为str复制给另一个变量，
都无法打印出what的表达式，只能打印出它的返回值。

即便 通过alist[:].index(a) 获取index来标记的方式也仅能取到头2个元素。

所以只好设置了一个变量来记录所处理到哪个元素。

"""
