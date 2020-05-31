#TempConvert.py

Tempstr=input("")
if Tempstr[0] in ['F','f']:
    C=(eval(Tempstr[1:55])-32)/1.8
    print("C{:.2f}".format(C))
elif Tempstr[0] in ['c','C']:
    F=1.8*eval(Tempstr[1:255])+32
    print("F{:.2f}".format(F))
else:
    print("")

