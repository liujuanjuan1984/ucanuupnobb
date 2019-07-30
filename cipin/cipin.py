def write_rlt(content,dic1,dic2):
    rlts = {}
    sum = 0
    for i in dic1.keys():
        for j in dic2.keys():
            ci = i + j
            if ci in content and ci not in rlts.keys() :
                num = content.count(ci)
                if  num > 1:
                    rlts[ci]=num
                    sum += 1
                    print(sum,"次")
    return rlts

def cipin_1(content):
    from string import punctuation,whitespace
    atext = punctuation + whitespace
    rlts = {}
    sum = 0
    for ci in content:
        if ci not in  atext and ci not in rlts.keys():
            num = content.count(ci)
            if num > 1:
                rlts[ci]=num
                sum += 1
                print(sum,"次")
    return rlts

def merge_dic(dic1,dic2):
    rlt = dic1.copy()
    rlt.update(dic2)
    return rlt

def cipin_x(content,dic1,dic2):
    rltsx = write_rlt(content,dic1,dic2)
    rltsy = write_rlt(content,dic2,dic1)
    rlts = merge_dic(rltsx,rltsy)
    return rlts

def sorted_dic(dic1,txt=None):
    rlt = sorted(dic1.items(),key=lambda x:x[1],reverse=True)
    print("\n--------------------\n")
    if txt==None:
        atxt = "结果共" 
    else:
        atxt = txt + "字词共"
    print(atxt,len(rlt),"条，具体为：\n",rlt)
    return rlt

def main():
    from content import book_x as content #加载想要统计的内容,string type
    import datetime
    import os.path

    rlt_url = 'D:/rlt.txt'

    with open(rlt_url,'at') as f:
        x = datetime.datetime.now()
        f.write(str(x))

    rlt1s = cipin_1(content)
    with open(rlt_url,'at') as f:
        f.write(str(sorted_dic(rlt1s,"单")))
        f.write(str(datetime.datetime.now()))

    rlt2s = cipin_x(content,rlt1s,rlt1s)
    with open(rlt_url,'at') as f:
        f.write(str(sorted_dic(rlt2s,"双")))
        f.write(str(datetime.datetime.now()))

    rlt3s = cipin_x(content,rlt1s,rlt2s)
    with open(rlt_url,'at') as f:
        f.write(str(sorted_dic(rlt3s,"3")))
        f.write(str(datetime.datetime.now()))

    rlt4s = cipin_x(content,rlt1s,rlt3s)
    with open(rlt_url,'at') as f:
        f.write(str(sorted_dic(rlt4s,"4")))
        f.write(str(datetime.datetime.now()))

    #rlt5s = cipin_x(content,rlt1s,rlt4s)
    #rlt6s = cipin_x(content,rlt1s,rlt5s)
    #rlt7s = cipin_x(content,rlt1s,rlt6s)


if __name__ == "__main__":
    main()
    print('词频统计完成。\n结果前往 D:/rlt.txt')