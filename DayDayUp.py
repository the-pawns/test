#DayDayUp



def upup(df):
   day=1
   for i in range(365):
      if i%7 in[6,0]:
         day=day*(1-0.01)
      else:
         day=day*(1+df)
   return day
dayfactor=0.01
while upup(dayfactor)<37.78:
   dayfactor+=0.001
print('工作日的努力参数是：{:.3f}'.format(dayfactor))
