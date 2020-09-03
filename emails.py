import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
from getpass import getpass

def send_mail(name, rollno, event_name, year, id, email, password):
    print(name, rollno)
    me = email
    you = f"{rollno}@iiitvadodara.ac.in"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Certificate"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html lang="en">
      <body>

        
        <div class="jumbotron">
          <p class="lead">Name:""" +str(name) + """</p>
          <p class="lead">RollNo:""" +str(rollno) + """</p>
          <p class="lead">Event:""" +str(event_name) + """</p>
          <p class="lead">Year: """ +str(year) + """</p>
          <p class="lead">ID: """ +str(id) + """</p>
           <a href="http://ec2-13-234-117-177.ap-south-1.compute.amazonaws.com/media/""" +str(id) + """.pdf" role="button">Certificate</a>
          <a class="btn btn-primary btn-lg" href="http://ec2-13-234-117-177.ap-south-1.compute.amazonaws.com/" role="button">Visit the website!</a>
        </div>

      </body>
    </html>

    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(email, password)
    mail.sendmail(me, you, msg.as_string())
    mail.quit()
    
    
email = input("Enter email ID: ")
password = getpass("Password: ")
event_name = input("Enter event name: ")
year = input("Enter event year: ")
dataset = pd.read_csv("generated.csv")

for i in range(len(dataset)):
    
    send_mail(dataset['Name'][i], dataset['RollNo'][i], event_name, year, dataset['Hash'][i], email, password)