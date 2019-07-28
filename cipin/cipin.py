def write_rlt(content,dic1,dic2):
    rlt = {}#有该结果但并没有用上
    rlts = {}
    sum = 0
    for i in dic1.keys():
        for j in dic2.keys():
            cix = i + j
            if cix in content:
                num = content.count(cix)
                if cix not in rlt.keys():
                    rlt[cix]=num
                    if num > 1:
                        rlts[cix]=num
                        sum += 1
                        if sum % 100 == 0:
                            print(sum,"次")
    return rlts

def cipin_1(content):
    from string import punctuation,whitespace
    atext = punctuation + whitespace
    rlt1 = {}
    rlt1s = {}
    sum = 0
    for ci in content:
        #r"[^\u4e00-\u9fa5^a-z^A-Z^0-9]"

        if ci not in  atext:
            num = content.count(ci)
            if ci not in rlt1.keys():
                rlt1[ci]=num
                if num > 1:
                    rlt1s[ci]=num
                    sum += 1
                    if sum % 100 == 0:
                        print(sum,"次")
    return rlt1s

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
    #print("---begin---",datetime.datetime.now())

    rlt1s = cipin_1(content)
    rlt2s = cipin_x(content,rlt1s,rlt1s)
    rlt3s = cipin_x(content,rlt1s,rlt2s)
    rlt4s = cipin_x(content,rlt1s,rlt3s)
    rlt5s = cipin_x(content,rlt1s,rlt4s)
    rlt6s = cipin_x(content,rlt1s,rlt5s)
    rlt7s = cipin_x(content,rlt1s,rlt6s)

    sorted_dic(rlt1s,"单")
    sorted_dic(rlt2s,"双")
    sorted_dic(rlt3s,"3")
    sorted_dic(rlt4s,"4")
    sorted_dic(rlt5s,"5")
    sorted_dic(rlt6s,"6")
    sorted_dic(rlt7s,"7")

    print("---end---",datetime.datetime.now())
    with open(rlt_url,'at') as f:
        f.write(sorted_dic(rlt1s,"单"))
        f.write(sorted_dic(rlt2s,"双"))
        f.write(sorted_dic(rlt3s,"3"))
        f.write(sorted_dic(rlt4s,"4"))
        f.write(sorted_dic(rlt5s,"5"))
        f.write(sorted_dic(rlt6s,"6"))
        f.write(sorted_dic(rlt7s,"7"))
        x = datetime.datetime.now()
        f.write(str(x))

if __name__ == "__main__":
    main()