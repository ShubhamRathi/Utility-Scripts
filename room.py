# -*- coding: utf-8 -*-

import csv
import sys
import smtplib

def Unique(your_list):
	if len(your_list)!=len(set(your_list)):
		return True
	return False

# Add Entry for Vrushank 
# Add Message for Vihar and Shantanu
# Add a list to store ferror names and error names
def form_email():
	f = open(sys.argv[1], 'rt')
	try:
	    reader = csv.reader(f)
	    ferror=[]
	    loop=1
	    for row in reader:
	    	if (row[1]=="manish"):	    		
		    	loop +=1
		        name= row[1]
		        if name=="Vihar Patel" or name=="Shantanu Parashar":	        	
		        	break;
		        email = row[2]
		        nom= row[3]
		        members="None"
		        if nom=="4":
		        	members="%s (%s), %s (%s), %s (%s), %s (%s)"% (row[4].strip(), row[5].strip(), row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip(), row[10].strip(), row[11].strip() )
		        if nom=="5":
		        	members="%s (%s), %s (%s), %s (%s), %s (%s), %s (%s)"% (row[12].strip(), row[13].strip(), row[14].strip(), row[15].strip(), row[16].strip(), row[17].strip(), row[18].strip(), row[19].strip(), row[20].strip(), row[21].strip() )
		        if nom=="6":
		        	members="%s (%s), %s (%s), %s (%s), %s (%s), %s (%s), %s (%s)"% (row[22].strip(), row[23].strip(), row[24].strip(), row[25].strip(), row[26].strip(), row[27].strip(), row[28].strip(), row[29].strip(), row[30].strip(), row[31].strip(), row[32].strip(), row[33].strip() )
		        p1=row[34].strip()
		        p2=row[35].strip()
		        p3=row[36].strip()
		        p4=row[37].strip()
		        pref= [p1,p2,p3,p4]
		        wing=row[38].strip()
		        A ="""Dear %s,\nThe following responses were recorded for your group:-\n""" % (name,)
		        B= """# of Members: %s\n""" % (nom,)
		        C= """Members: %s\n""" % (members,)
		        D= """Floor Preferences: %s > %s > %s > %s\n""" %(p1,p2,p3,p4,)
		        E= """Wing Preferences: %s\n""" %(wing,)	        
		        if (Unique(pref)):
		        	F="""We'd like to draw your attention to a discrepancy we've noted in your entry. We're expecting that your floor preferences be unique.\nPlease fill this form: http://goo.gl/forms/v0RFtmCh4n to inform us of your updated floor preferences.\n"""
		        	ferror.append(name)        	
		        else:
		        	F="""Should you want to notify us of any changes, please do so by filling this form: http://goo.gl/forms/v0RFtmCh4n by 1st July, 10 pm.\n"""
		        G= """Do forward this email to other members of your group.\n"""
		        H="""Regards,\nHostelCom"""
		        content=A+B+C+D+E+F+G+H
		        msg = """From: hostelcom@hostelcom\nTo: %s\nSubject: Your Room Allocation Response\n""" %email
		        msg = msg + content
		        server = smtplib.SMTP_SSL('research.iiit.ac.in', port=465)
		        server.set_debuglevel(1)
		        server.ehlo
		        server.login('shubham.rathi', 'Duucatibikee123Du')
		        server.sendmail('shubham.rathi@research.iiit.ac.in', [email], msg)
		        server.quit()
	except:
		print "___________________________________________________________________________________________________________"
		print name
		print "___________________________________________________________________________________________________________"

	finally:
		f.close()
		

form_email()