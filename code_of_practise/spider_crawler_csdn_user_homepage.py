"""
一个简单的爬虫脚本，爬取指定用户的个人主页。比如可用于监测自己csdn文章的阅读、回复等数据变化。

author:liujuanjuan1984
date:2019-09-11

"""

import datetime
import re
import urllib.request
import pandas as pd
import random
import pymysql
import os.path

from sqlalchemy import create_engine
conn = create_engine('mysql+pymysql://root:password@localhost:3306/zhihuclawer',encoding='utf8')  

csdn_path = 'D:/crawler/output_csdn/'
wf_log = open(csdn_path + 'log_csdn_my_article.txt', 'at')

# 读取网页，把读取的数据返回为一个移除了换行空格等符号的 str 对象，供后续 re 处理调用
def read_url(url):
    #header库实现随机header，一定程度上克制反爬
    headers_list = [
        ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.112 Safari/537.38"),
    ]
    rand = random.randint(1,len(headers_list))
    opener = urllib.request.build_opener()
    opener.addheaders = headers_list.copy()[rand-1:rand]
    data = opener.open(url).read()
    html_text = str(data,encoding='utf-8')
    html_text = clean_str(html_text)
    return html_text

def clean_str(str_obj):
    str_obj = str_obj.replace('\n','')
    str_obj = str_obj.replace('\t','')
    str_obj = str_obj.replace(' ','')
    str_obj = str_obj.replace('　','')
    str_obj = str_obj.replace('\r','')
    return str_obj

def read_a_page(url):
    html_text = read_url(url)
    attn = r'<h4class=""><ahref="(.*?)"target="_blank"><spanclass="article-typetype-(.*?)float-none">(.*?)</span>(.*?)</a></h4><pclass="content"><ahref="(.*?)"target="_blank">(.*?)</a></p><divclass="info-boxd-flexalign-content-center"><p><spanclass="date">(.*?)</span></p><pclass="point"></p><p><spanclass="read-num">阅读数<spanclass="num">(.*?)</span></span></p><pclass="point"></p><p><spanclass="read-num">评论数<spanclass="num">(.*?)</span></span></p></div></div>'
    result = re.findall(attn,html_text,re.S)
    if result:
        article_df = pd.DataFrame(result,columns=['articlt_url','articlt_itype','articlt_type','articlt_title','articlt_url_2','articlt_desct','press_time','read_count','reply_count'])
        article_df['update_time'] = str(datetime.datetime.now())
        pd.io.sql.to_sql(article_df, "csdn_my_article", conn, if_exists='append', index=False)
        print(datetime.datetime.now(),url,'is done.')
        wf_log.write(str(datetime.datetime.now()) + str(url) + 'is done.\n')
    return article_df

def read_all_pages(pages=5,csdn_id='qiaoanlu'):
    print(datetime.datetime.now(),'read_all_pages ...')
    wf_log.write(str(datetime.datetime.now()) + 'read_all_pages ... args:' + str(pages) + ', ' + csdn_id+'\n')
    for i in range(1,pages+1):
        url = 'https://blog.csdn.net/' + csdn_id + '/article/list/' + str(i) + '?'
        try:
            read_a_page(url)
        except:
            print(datetime.datetime.now(),'some error happended',i)
            wf_log.write(str(datetime.datetime.now()) + str(i) +'some error happended')
            continue
    print(datetime.datetime.now(),'read_all_pages is done.')
    wf_log.write(str(datetime.datetime.now()) +'read_all_pages is done.\n')

def output_file():
    conn = pymysql.connect('localhost','root','789351','zhihuclawer')
    cursor = conn.cursor()
    sql_search = 'select * from csdn_my_article;'
    csdn_my_article = pd.read_sql(sql_search,conn)
    cursor.close()
    conn.close()

    rlt_url = csdn_path + 'csdn_my_article'+str(datetime.datetime.now())[:10]+'.csv'
    csdn_my_article.to_csv(rlt_url, encoding='utf_8_sig', index=False)

    print('文件已生成',rlt_url)
    wf_log.write(str(datetime.datetime.now()) + ' output_file is done.' + '\n')
    return csdn_my_article

def main():
    read_all_pages(pages=5,csdn_id='qiaoanlu')
    output_file()

if __name__ == "__main__":
    main()