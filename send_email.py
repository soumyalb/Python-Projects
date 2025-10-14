# Problem Statement:
# You want to write a Python program that can send emails to one or multiple recipients using an email account.

# Question:
# How can I write a Python program that can send emails to one or multiple recipients using an email account?

# Using smtplib Simple Mail Transfer Protocol (SMTP)

# Import the smtplib library
import smtplib

sender_email = "xx@gmail.com"
sender_email_password = "xxxx"
receiver_email = "xx@gmail.com"

# Create a session 
s= smtplib.SMTP('smtp.gmail.com',587)

# Put smtp in security mode i.e. tls mode
s.starttls()

# Sender emailid and password
s.login(sender_email, sender_email_password)

# Message
message = "Hello \n" \
"this message sent using Python."

# Receiver details
s.sendmail(sender_email, receiver_email, message)

# Terminate
s.quit()

