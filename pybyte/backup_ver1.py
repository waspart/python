import os
import time

# 1. 需要备份的文件与目录将被指定在一个列表中
source = ['''D:\\python\\hello.py''', '''D:\\python\\runoob''']

# 2. 备份文件必须存储在一个主备份目录中
target_dir = r'D:\\python\\backup'

# 3. 备份文件将被打包压缩成zip文件
# 4. 压缩文件的文件名称由当前日期与时间构成
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. 使用zip命令进行压缩，Unix系统下
zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

# 6. 运行备份
print('Zip Command is: ')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
    print('successful backup to ', target_dir)
else:
    print('backup failed')
