#!/usr/bin/python3
# File name   : motor.py
# Description : Control Motors 
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

import os
import time

def replace_num(file,initial,new_num):  
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)

for x in range(1,4):
	if os.system("sudo apt-get update") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y samba samba-common-bin") == 0:
		break

try:
	replace_num("//etc/samba/smb.conf",';   write list = root, @lpadmin',';   write list = root, @lpadmin\n\n[NASshare]\n   comment = raspberry\n   valid users = pi,root\n   path = /home/\n   browseable = yes\n   writable = yes\n   create mask = 0777\n   directory mask = 0777')
except:
	pass

for x in range(1,4):
	print('your password?')
	if os.system("sudo smbpasswd -a pi") == 0:
		break

for x in range(1,4):
	if os.system("sudo /etc/init.d/samba restart") == 0:
		break

print('name NASshare')