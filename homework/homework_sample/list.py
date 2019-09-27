
alist = ['liu','juan','juan']

for a in alist:
    print(a,alist.index(a))
    for x in a:
        print(x,a,a.index(x))

acount = alist.count("juan")
print('次数是',acount)



"""
#这就是无限循环本尊了。可以拷贝这段去新建一个.py文件运行试试。
alist = ['liu','juan','juan']
for y in alist : 
    alist.append('@') 
    print(y,alist)
"""

#列表不切片，直接对列表操作，导致了列表被改变。
#此段代码很容易陷入无限循环，只有通过breakTag来实现循环次数控制。
breakTag = 4
for y in alist : # 原本以为列表有3个元素，会遍历3次
    breakTag = breakTag - 1
    if breakTag > 0 :
        alist.append('@') #但这个操作让每一次遍历就会增加1个元素，并回归到 for 那句判断，从而导致无限循环。
        print(y,alist)
print("\n开始演示切片控制列表被改变所带来的影响\n")
dlist = ['liu','juan','juan']
blist = dlist[:]
for y in dlist:#并没有操作dlist，所以无需担心无限循环。
    dlist[:].append('@')
    blist.append("$")
    print(y,'：此时dlist是',dlist)
    print(y,'：此时dlist[:]是',dlist[:])
    print(y,'：此时blist是',blist)
