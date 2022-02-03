import os

#shadacc = os.access('/home/prepod',os.W_OK)
#dost = os.system('ls -l /etc/shadow')
testping = os.system('ping 8.8.8.8 -c 1  > /dev/null')
print(testping)

#print(shadacc)
#print(dost)
#print(testping)
