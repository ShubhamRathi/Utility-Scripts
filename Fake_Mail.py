import smtplib
 

msg = """From: pmo@pmindia.gov.in
To: talk2mealways@gmail.com
Subject: Your Room Allocation Response\n  
""" %email 
server = smtplib.SMTP_SSL('research.iiit.ac.in', port=465)
server.set_debuglevel(1)
server.ehlo
server.login('shubham.rathi', 'Duucatibikee123Du')
server.sendmail('shubham.rathi@research.iiit.ac.in', ['talk2mealways@gmail.com'], msg)
server.quit()