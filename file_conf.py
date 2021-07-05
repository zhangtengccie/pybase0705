#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng
import os
# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1','w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2','w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3','w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
print('文件夹包含"qytang"关键字的文件为：')
print('方案一:')
list1 = []

os.chdir('test')
for f in os.listdir(os.getcwd()):
    if os.path.isfile(f):
        for line in open(f,encoding='UTF8'):
            if 'qytang' in line:
                list1.append(f)

for i in list1:
    print(i)
print('方案二：')
list2 = []
list3 = []
for root,dirs,files in os.walk(os.getcwd()):
    # print(files)
    if 'qytang1' in files:
        list2.append(files)

for i in list2[0]:
    for line in open(i):
        if 'qytang' in line:
            list3.append(i)

for i in list3:
    print(i)

os.chdir('..')
for root,dirs,files in os.walk('test',topdown=False):
    for name in files:
        os.remove(os.path.join(root,name))
    for name in dirs:
        os.rmdir(os.path.join(root,name))
os.removedirs('test')