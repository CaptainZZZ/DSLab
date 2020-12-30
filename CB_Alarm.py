# -*- coding: utf-8 -*-
import time
from smtplib import SMTP_SSL

def sendemail(addrs):
	server=SMTP_SSL('smtp.gmail.com',465)
	server.login('dsimakovlab@gmail.com','password')
	msg=('CB Alarm')
	server.sendmail('dsimakovlab@gmail.com',addrs,msg)
	server.quit()

def thingsareok(filename):
	f=open(filename,mode='r',encoding='utf-8')
	i=0
	data=f.readlines()
	CB=float(data[len(data)-1].split('\t')[1])
	print(CB)
	t=float(data[len(data)-1].split('\t')[0])
	f.close()
	return t,CB
t=0
p=0
addrs=input('Paste email address ')
filename=input('Paste the file name here ')
while True:
	i=thingsareok(filename)
	if i[0]==t:
		break
	t=i[0]
	if i[1]<50 or i[1]>150:
		if t>=14400:
			if p==0:
				print('Carbon balance went off at ',time.asctime())
				sendemail(addrs)
				p=1
	time.sleep(10)
	
