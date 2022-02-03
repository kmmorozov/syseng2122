import os


print(os.getpid()) 
print(os.cpu_count())
print(os.getcwd())
print(os.getenv('HOME'))
print(os.getenv('USERNAME'))
print(os.getenv('PATH'))
print(os.getenv('LANG'))
print(str(os.getenv('HOME')+'/'+os.getenv('USERNAME')))

os.mkdir(str(os.getenv('HOME')+'/'+os.getenv('USERNAME')))

dirstr = str(os.getenv('HOME'))
ndirstr = str(os.getenv('USERNAME'))

#print(dirstr)
#print(ndirstr)
#allpath = dirstr+'/'+ndirstr
#print(allpath)
#os.mkdir(allpath)


mem = os.system('ls')
print(type(mem))


#os.mkdir('/home/prepod/123')
