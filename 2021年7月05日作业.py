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
for file_or_dir in os.listdir(os.getcwd()):
    if os.path.isfile(file_or_dir):
        for line in open(file_or_dir):
            if 'qytang' in line:
                print('\t'+file_or_dir)
                break
print('方案二：')
list2 = []
list3 = []
for root,dirs,files in os.walk(os.getcwd(),topdown=False):
    print(files)
    for file_name in files:
        for line in open(os.path.join(root,file_name)):
            if 'qytang' in line:
                print('\t' + os.path.join(root,file_name))
                break