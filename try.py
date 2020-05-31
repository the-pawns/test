def processFile(inputFile, outputFile):                         #定义一个函数
    fin = open(inputFile, 'r')                                  #以读的方式打开文件
    fout = open(outputFile, 'w')                                #以写得方式打开文件
    for eachLine in fin:                                        #读取文件的每一行
        line = eachLine.strip().decode('utf-8', 'ignore')       #去除每行的首位空格，并且将文件编码转换成Unicode编码
        outStr = line                                           #我没对读入的文本进行处理，只是直接将其输出到文件
        fout.write(outStr.strip().encode('utf-8') + '\n')       #去除首位的空格，并转回到utf-8编码，然后输出
    fin.close()                                                 #关闭文件
    fout.close()
 
processFile('myinputFile.txt', 'myoutputFile.txt')              #调用该函数对文件进行处理
