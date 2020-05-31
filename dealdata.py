import pandas as pd
import matplotlib.pyplot as plt
#读数据
df=pd.read_csv('data.csv',encoding='cp936')
df=df.dropna()
#生成营业额折线图
plt.figure()
df.plot(x=df['日期'])
plt.savefig('jpg')

#按月统计，生成柱状图
plt.figure()
df1=df[:]
df1['month']=df1['日期'].map(lambda x: x[:x.rindex('-')])
df1.plot(x=df1['month'],kind='bar')
plt.savefig('second.jpg')
