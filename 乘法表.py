
for i in range(1,10):
    for j in range(1,i+1):
        sum_1 = i*j
        if i == j:
            print("{: >2}".format(i),"x","{: >2}".format(j),"=","{: >2}".format(sum_1))    #分支用于判断是否需要转行
        else:
            print("{: >2}".format(i),"x","{: >2}".format(j),"=","{: >2}".format(sum_1),end = ' ') #end 默认情况下是以换行符结尾，此处申明以空格结尾

print('')
for i in range(1,10):
    for j in range(i,10):
        sum_2 = i*j
        if j == 9:
            print("{: >2}".format(i),"x","{: >2}".format(j),"=","{: >2}".format(sum_2))
            print(' '*13*i,end = '')   #占位显示为空，呈现倒三角效果,此处我规定一条乘法口诀占用13个字符
        else:
            print("{: >2}".format(i),"x","{: >2}".format(j),"=","{: >2}".format(sum_2),end = ' ')



