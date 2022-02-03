import subprocess
import os

#os.system('gedit')
#print('1')
#subprocess.call("gedit")
#print('2')
#subprocess.Popen('gedit')
#print('3')



#process = subprocess.Popen('ping -c 1 8.8.4.4')
#code = process.wait()
#data=os.system('ping -c 1 8.8.8.8')
code=subprocess.Popen(['ping','-c','1','8.8.4.4'])
code = process.wait()
    
    