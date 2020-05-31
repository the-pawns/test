import turtle as t
import wordcloud
f=open('新时代中国特色社会主义.txt','r',encoding='utf-8')
t=f.read()
t.setup(1000,1000)
t.penup()
t.pendown()
t.pensize(25)
t.pencolor('purple')
for i in range(5):
    t.fd(200)
    t.seth(-72*(i+1))
    
t.penup()
t.forward(200)
t.pendown()
t.pensize(25)
t.pencolor('red')
for i in range(5):
    t.fd(200)
    t.seth(-72*(i+1))

