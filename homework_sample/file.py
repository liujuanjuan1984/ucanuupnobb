#获取文件地址
import os
import os.path

a_file_data_path = 'D:/liujuanjuan/vscode/ucanuupnobb/file_sample/afiledata.txt'

def main():
    for x in range(100):
        check_readline(x)




#检查文件是否存在




#读取文件内容，并处理

#用with语句无需file.close()
"""
with open(a_file_data_path,'rt',encoding = 'utf-8') as f:
    x = f.readline()
    print(x)
    y = f.readlines()
    print(y)
    pass

"""


def check_readline(x):
    with open(a_file_data_path,'rt',encoding = 'utf-8') as f:
        y = f.readline(x)
        print(x,y)


def check_readlines(x):
    with open(a_file_data_path,'rt',encoding = 'utf-8') as f:
        y = f.readlines()
        print(y)
        

#读取指定行


#写入文件（覆盖写，不覆盖写，每次写入前清空之前的内容）


main()