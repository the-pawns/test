# -*- coding:utf-8*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import requests
from lxml import etree
time1=time.time()
import pandas as pd


df = pd.read_csv('F:/IDcard.xlsx', sep='\t', header=None, dtype=str, na_filter=False)
print df
idcard=[]
sex1 = []
birthday1 = []
address1 = []

length=len(df)
for i in range(0,length):
    try:
        print df.iloc[i,0]
        idcard.append(df.iloc[i,0])
        url="http://qq.ip138.com/idsearch/index.asp?action=idcard&userid="+df.iloc[i,0]+"&B1=%B2%E9+%D1%AF"
        html=requests.get(url).content
        selector=etree.HTML(html)
        sex=selector.xpath('//td[@class="tdc2"][1]/text()')
        for each in sex:
            print each
            sex1.append(each)

        birthday=selector.xpath('//td[@class="tdc2"][2]/text()')
        for each in birthday:
            print each
            birthday1.append(each)

        address=selector.xpath('//td[@class="tdc2"][3]/text()')
        for each in address:
            print each
            address1.append(each)
    except Exception, ex:
        print Exception, ":", ex

data=pd.DataFrame({'idcard':idcard,'sex':sex1,'birthday':birthday1,'address':address1})
print (data)
pd.DataFrame.to_excel(data,"F:\\person_card.xlsx",header=True,encoding='gbk',index=False)
time2=time.time()
print u'ok,爬虫结束!'
print u'总共耗时：'+str(time2-time1)+'s'
