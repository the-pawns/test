import csv
import random
import datetime
fn ='data.csv'
with open(fn,'w')as fd:
    wr=csv.writer(fd)
    wr.writerow(['日期','销量'])
    startDate=datetime.date(2017,2,21)
    for i in range(365):
        amount=300+i*5+random.randrange(100)
        wr.writerow([str(startDate),amount])
        #下一天
        starDate=startDate+datetime.timedelta(days=1)
        
