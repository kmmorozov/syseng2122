##for i in 'kirill','stephan','serg','fedor':
##    print(i)
file = open('/home/prepod/file2.txt','r')

for i in file:
    #print(type(line))
    subline=i.split(':')
    print(subline)
    #print(type(subline))
   # print(subline)
    print(subline[0])
    print(subline[1])

file.close()