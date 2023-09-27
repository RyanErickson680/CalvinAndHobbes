import smtplib
import datetime
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 


#--------------------------------------------------
addr_from = ' '

smtp_server = 'smtp.gmail.com'
smtp_port   = 587
#smtp_user   = 'erirya680@gmail.com'
smtp_user = 'daily.calvin.hobbes@gmail.com'
#smtp_pass   = 'hwvi acnk ebxf yjkp'
smtp_pass = 'lach bfct avii hqco'

#--------------------------------------------------------------

def sendText(to, image1, text=''):
		addr_to = to

		# Get date and time and add it to the text message
		#now = datetime.datetime.now().strftime('%B-%d-%Y %H:%M:%S')

		msg = MIMEMultipart()
		msg['To'] = addr_to

		#msgText.set_charset("ISO-8859-1")
		msgText = MIMEText(text)
		#msg.attach(msgText)

		file1 = open(image1, 'rb')
		attachment1 = MIMEImage(file1.read())
		file1.close()

		attachment1.add_header('Content-Disposition','attachment',filename=image1)

		msg.attach(attachment1)

		# Send the message via an SMTP server
		s = smtplib.SMTP(smtp_server,smtp_port)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(smtp_user,smtp_pass)
		s.sendmail(addr_from, addr_to.split(","), msg.as_string())

		s.quit()