f = open('/proc/meminfo','r')
str = f.readline()


str = str.split(' ')
#print(type(str))
print(str[7])
    
    