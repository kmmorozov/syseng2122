import os

testping = os.system('ping 10.1.6.145 -c 1  > /dev/null')

print(testping)