import os
#print('\n'.join(dir(os)))
##print(os.times())
print(os.getcwd())
#print(os.getgid())
##print(os.getpid())
##print(os.getlogin())
print(os.listdir())
print(os.path.isfile('TestDate.py'))
os.system('dir')
n=1
while n!=10:
    os.rename('Testdatei.txt','Testdatei'+str(n)+'.txt')
    os.system('copy Testdatei1.txt Testdatei.txt')
    n += 1