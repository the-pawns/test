import matplotlib.pyplot as plt
labels= 'a','b','c','d','e'
sizes=[15,30,30,15,10]
explode=(0,0.1,0,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow =False,startangle=90)
plt.axis('equal')
plt.show()