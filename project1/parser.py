import os
os.path.join('usr', 'bin', 'spam')
myFiles = ['log.txt', 'kernlog.txt','dmesg.log']
#create OS path
for filename in myFiles:
	print(os.path.join('/home/dracos/dailycode/project1', filename))
#print(os.path.join('/home/dracos/dailycode/project1'))

#Open and Reading Contents
#print os.getcwd()
#read('/home/dracos/dailycode/project1')
log = open('/home/dracos/dailycode/project1/log.txt')
log.readlines()
kernlog = open('/home/dracos/dailycode/project1/kern.log')
dmesg = open('/home/dracos/dailycode/project1/dmesg.log')
Rlog = log.read()
Rkern = kernlog.read()
Rdmesg = dmesg.read()
print(Rlog)
#print '$Rkern'
#print '$Rdmedg'
