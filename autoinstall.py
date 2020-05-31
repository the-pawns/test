import os
libs={'csv','pandas ','datetime','matplotlib.pyplot'}
try:
    for lib in libs:
        os.system("pip install"+lib)
        print('successful')
except:
    print('Failed somehow')
