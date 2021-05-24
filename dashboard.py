labelusername=""
remotesshwebserverusername=""
remotesshwebserverpw=""
remotesshwebserverip=""
remotesshwebserverdir=""
localsshwebserverdir=""
remotemysqluser=""
remotemysqlpw=""
remotemysqldb=""

import commands
import os
from time import sleep
import datetime
while (1):
	os.system("clear")
	print("1.Start Nginx")
	print("2.Stop Nginx")
	print("3.Status Nginx")
	print("4.Enable Nginx")
	print("5.Disable Nginx")
	print("----------------")
	print("6.Start Gunicorn")
	print("7.Stop Gunicorn")
	print("8.Status Gunicorn")	
	print("9.Enable Gunicorn")	
	print("10.Disable Gunicorn")	
	print("----------------")
	print("11.Port Listening")
	print("12.Edit nginx conf")
	print("13.Edit Gunicorn conf")
	print("14.Daemon-reload services")
	print("----------------")	
	print("15.chmod static folder 755")
	print("----------------")
	print("20.Mount remote forpsi")
	print("21.Backup remote DB")
	print("----------------")
	
	print("66.logz one/catch200.log one/catchnot200.log")
	print("77.logz /var/log/nginx/error.log access.log")
	print("88.Make db backup to Documents/backup_mysql")
	print("99.Exit")
	print("__________________")
	val = input("Enter your value: ")
	if int(val)==1:
		os.system("clear")
		os.system("sudo systemctl start nginx")
	elif int(val)==2:
		os.system("clear")
		os.system("sudo systemctl stop nginx")
	elif int(val)==3:
		os.system("clear")
		os.system("sudo systemctl status nginx")
		raw_input("Press Enter to continue...")
	elif int(val)==4:
		os.system("clear")
		os.system("sudo systemctl enable nginx")
	elif int(val)==5:
		os.system("clear")
		os.system("sudo systemctl disable nginx")
	elif int(val)==6:
		os.system("clear")
		os.system("sudo systemctl start gunicorn")
	elif int(val)==7:
		os.system("clear")
		os.system("sudo systemctl stop gunicorn")
	elif int(val)==8:
		os.system("clear")
		os.system("sudo systemctl status gunicorn")
		raw_input("Press Enter to continue...")
	elif int(val)==9:
		os.system("clear")
		os.system("sudo systemctl enable gunicorn")
	elif int(val)==10:
		os.system("clear")
		os.system("sudo systemctl disable gunicorn")		
		
		
		
	elif int(val)==11:
		os.system("clear")
		print("---------------------")
		os.system("sudo lsof -i -P -n | grep LISTEN")
		raw_input("Press Enter to continue...")
	elif int(val)==12:
		os.system("clear")
		#os.system("sudo nano /etc/nginx/sites-available/one")	
		os.system("sudo nano /etc/nginx/conf.d/default.conf")	
		os.system("clear")
	elif int(val)==13:
		os.system("clear")
		os.system("sudo nano /etc/systemd/system/gunicorn.service")		
		os.system("clear")

	elif int(val)==14:
		os.system("clear")
		os.system("sudo systemctl daemon-reload")		
		os.system("clear")
	elif int(val)==15:
		os.system("sudo chmod 755 -R /home/%s/Documents/one/one/static/" % labelusername)
		os.system("clear")
	elif int(val)==20:
		os.system("sshfs -o password_stdin -d %s@%s:/%s /%s <<< '%s' &" %(remotesshwebserverusername,remotesshwebserverip,remotesshwebserverdir,localsshwebserverdir,remotesshwebserverpw))
		#os.system("clear")		
	elif int(val)==21:
		os.system("sshpass -p %s ssh %s@%s mysqldump --single-transaction --no-tablespaces -u %s -p%s %s > %s" % (remotesshwebserverpw,remotesshwebserverusername,remotesshwebserverip,remotemysqluser,remotemysqlpw,remotemysqldb,remotemysqldb))
		#zip biotalconnect.zip biotalconnect
	elif int(val)==66:
		os.system("multitail -cS goldengate %scatch200.log -cS goldengate %scatchnot200.log" % (localsshwebserverdir,localsshwebserverdir))
	elif int(val)==77:
		os.system("multitail %saccess.log %serror.log" % (localsshwebserverdir,localsshwebserverdir))
	elif int(val)==88:
		os.system("clear")
		now = datetime.datetime.now()
		timestamp = str(now.strftime("%Y_%m_%d_%H_%M_%S"))
		os.system("sudo mysqldump --defaults-file=/root/.my.cnf --all-databases > %sbackup_mysql/mysql_%s.sql" % (remotesshwebserverdir,timestamp))
		os.system("clear")
		os.system("ls -lt %sbackup_mysql/" % remotesshwebserverdir)
		raw_input("Press Enter to continue...")


	
	elif int(val)==99:
		print "EXIT"
		break
