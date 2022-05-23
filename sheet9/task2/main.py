import time
from file import File
from directory import Directory


d1 = Directory(name='mydir', owner='sepehr')
d2 = Directory(name='root', owner='sepehr')

time.sleep(5)

f1 = File(name='file1.txt', owner='sepehr', size='10240')
f2 = File(name='file2.txt', owner='sepehr', size='46')
f3 = File(name='file3.txt', owner='sepehr', size='73323')
f4 = File(name='file4.txt', owner='sepehr', size='167024')
f5 = File(name='file5.txt', owner='sepehr', size='1337')


d1.add(f1)
d1.add(f2)
d1.add(f3)
d1.add(f4)

d2.add(d1)
d2.add(f5)

d1.list()
print('-------------------------')
d2.list()