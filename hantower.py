#hantower
count=0
def hanoi(n,r,l,m):
    global count
    if n==1 :
        print('{}:{}->{}'.format(1,r,l,))
        count+=1
    else :
        hanoi(n-1,r,m,l)
        print('{}:{}->{}'.format(n,r,l))
        count+=1
        hanoi(n-1,m,l,r)
hanoi(30,'a','b','c')
