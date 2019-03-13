import os
import os.path

"""
题目：
文章统计所有字符（统计英文[大小写不敏感]，数字；其他符号不计算）的出现次数，并按照次数倒序输出

a:1001
c:888
1:12
3:5

"""

testFile ='D:/liujuanjuan/vscode/ucanuupnobb/testyourself/test_yourself_001.txt'

def main():
    with open(testFile,'rt',encoding='UTF-8') as f:
        blines = f.readlines()
    
    aList = get_chars(blines)
    muchtimesDic = count_chars(aList,blines)

    keys = muchtimesDic.keys()
    vals = muchtimesDic.values()
    rlist = [(key,val) for key,val in zip(keys,vals)]

    Rlist = sorted(rlist,key = lambda x:x[1],reverse = True)
    for i in Rlist:
        print(i[0],i[1])
    print(Rlist)   

def get_chars(blines):
    """
    功能：获取待检索的字符列表。通过遍历文本，把所有出现的字符列举出来。（大小写不敏感）
    """
    aList = []
        
    for aline in blines:
        aline = aline.lower()
        bline = aline[:]
        for i in bline:
            if i not in aList :
                aList.append(i)
    return aList


def count_chars(aList,blines):
    """
    功能：统计字符出现的次数，并返回字典。
    """
    muchtimesDic = {}

    for i in aList:
        howmanytimes = 0
        for aline in blines:
            aline = aline.lower()
            bline = aline[:]        
            if i in bline:
                howmanytimes = bline.count(i) + howmanytimes
        muchtimesDic[i] = howmanytimes
    return muchtimesDic


main()