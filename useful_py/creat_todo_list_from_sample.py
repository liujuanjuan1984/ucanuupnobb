import os
import os.path

"""
功能：采用模板便捷地生成指定日期的待办清单。
"""

MyToToPath = 'D:/liujuanjuan/vscode/records/todo/'


#指定日期，并创建该日期的文件。
whichDAY = input('请输入日期，格式为：20190228\n\n')
yy=whichDAY[:4]
mm=whichDAY[4:6]
dd=whichDAY[6:]
thisDAY = str(yy) + '年' + str(mm) + '月' + str(dd) + '日：\n'


whenFile = MyToToPath + str(whichDAY) + '.md'
sampleFile = MyToToPath + 'todosample.md'
sf = open(sampleFile,'rt', encoding='utf-8')
f = open(whenFile,'at', encoding='utf-8')

f.write(thisDAY)

for line in sf.readlines():
    f.write(line)

f.close()
sf.close()


