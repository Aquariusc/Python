#!/E/Lucifer/Python/Code
#!Filename:Backup_ver2.py

import os
import time

#1.The files and directories to be backed up are specified in a list.
source=[r'E:\Lucifer\Python\Code\Dir.py'] #要备份的文件路径
#If you are using Windows,use source=[r'C:\Documents',r'D:\Work'] or something like that

#2.The backup must be stored in a main backup directory
target_dir=r'E:\Lucifer\Python' #备份文件存放位置

#3.The files are backed up in to a rar file.

#4.The current day is the name of the sub directory in the main directory
today=target_dir+time.strftime('%Y%m%d')
#The current time is the name of the rar archive
now=time.strftime('%H%M%S')

#Create the sub directory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) #make directory
    print('Successfully created directory',today)

#The name of the rar file
target=today+os.sep+now+'.rar'

#5.We use the zip command(in Unix/Linux) to put the files in a zip archive
rar_command='"E:\Lucifer\Python\Rar.exe" a %s %s'%(target,' '.join(source)) #使用rar命令备份

#Run the backup
if os.system(rar_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
