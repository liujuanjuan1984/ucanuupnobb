def cipin_x(content,dic1,dic2):
    rlts = {}
    for i in dic1.keys():
        for j in dic2.keys():
            if dic2[j] <= dic1[i]:
                ci = i + j
                cix = j + i
                if ci in content and ci not in rlts.keys() :
                    num = content.count(ci)
                if cix in content and ci not in rlts.keys() :
                    numx = content.count(cix)
                    if  num > 1:
                        rlts[ci]=num
                    if numx > 1:
                        rlts[cix]=numx
    #rlts = sorted(rlts.items(),key=lambda x:x[1],reverse=True)
    return rlts

def cipin_1(content):
    from string import punctuation,whitespace
    atext = punctuation + whitespace
    rlts = {}
    for ci in content:
        if ci not in  atext and ci not in rlts.keys():
            num = content.count(ci)
            if num > 1:
                rlts[ci]=num
    #rlts = sorted(rlts.items(),key=lambda x:x[1],reverse=True)
    return rlts

def main():
    from content import book_x as content #加载想要统计的内容,string type
    import datetime
    import os.path
    
    x = str(datetime.datetime.now())
    rlt_url = 'D:/rlts' + x[-6:] + '.txt'

    with open(rlt_url,'at') as f:
        f.write('\n'+str(datetime.datetime.now())+'\n')

    rlt1s = cipin_1(content)
    with open(rlt_url,'at') as f:
        f.write(str(rlt1s))
        f.write('\n'+str(datetime.datetime.now())+'\n')

    rlt2s = cipin_x(content,rlt1s,rlt1s)
    with open(rlt_url,'at') as f:
        f.write(str(rlt2s))
        f.write('\n'+str(datetime.datetime.now())+'\n')

    rlt3s = cipin_x(content,rlt1s,rlt2s)
    with open(rlt_url,'at') as f:
        f.write(str(rlt3s))
        f.write('\n'+str(datetime.datetime.now())+'\n')

    rlt4s = cipin_x(content,rlt1s,rlt3s)
    with open(rlt_url,'at') as f:
        f.write(str(rlt4s))
        f.write('\n'+str(datetime.datetime.now())+'\n')

    #rlt5s = cipin_x(content,rlt1s,rlt4s)
    #rlt6s = cipin_x(content,rlt1s,rlt5s)
    #rlt7s = cipin_x(content,rlt1s,rlt6s)


if __name__ == "__main__":
    main()
    print('词频统计完成。\n结果前往 D:/rlt.txt')