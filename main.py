import smtplib, ssl, csv 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# sender_email = input("Type your email and press enter:")
# password = input("Type your password and press enter:")



message = MIMEMultipart("alternative")

# ENTER SUBJECT OF MAIL
message["Subject"] = "ADG Mobile Application Launch 📱"

message['From'] = formataddr(('Apple Developers Group VIT', sender_email))

# Create the HTML version of your message
html = """\
<html>
  <body>
  
    <h1> Hi  </h1><br>
    <center><img height="500px" width=500px" src="https://raw.githubusercontent.com/ADG-VIT/Email-Script/master/POSTER.png"></center>

    <div style="background-color:#191919; color: white; padding: 5px; padding-left: 10px; padding-right: 10px; border-radius: 5px;">
        <h4>ABOUT<h4>
        <p style="font-weight: normal; padding-left: 10px;">Apple Developers Group (ADG) is a name synonymous with excellence, simplicity and dedication. It is a registered student community at VIT, Vellore established under the Apple University program. A coterie of talented minds seeking not just success but perfection.</p>

        <h4>SOCIAL</h4>
        <ul style="line-height: 200%; padding-left: 10px; list-style: none;">
            <li><a style="padding-left: 10px; color: white;" href="https://www.facebook.com/vitios/" target="_blank"><img src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/facebook-logo-min.png" style="width: 18px; height: 18px; float: left; overflow: hidden;"> Facebook</a></li>
            <li><a style="padding-left: 10px; color: white;"  href="https://www.linkedin.com/company/adgvit/" target="_blank"><img src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/linkedin-logo-min.png" style="width: 18px; height: 18px; float: left; overflow: hidden;"> LinkedIn</a></li>
            <li><a style="padding-left: 10px; color: white;"  href="https://www.instagram.com/adgvit/" target="_blank"><img src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/instagram-logo-min.png" style="width: 18px; height: 18px; float: left; overflow: hidden;"> Instagram</a></li>
            <li><a style="padding-left: 10px; color: white;"  href="https://twitter.com/adgvit" target="_blank"><img src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/twitter-2-min.png" style="width: 18px; height: 18px; float: left; overflow: hidden;"> Twitter</a></li>
        </ul>
        <h5 align="center">Copyright © 2020 All rights reserved</h5>
    </div>
  </body>
</html>
"""

# Turn into html MIMEText objects
part = MIMEText(html, "html")

# Add HTML part to MIMEMultipart message
message.attach(part)

# Create secure connection with server and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)

    with open('result.csv', 'w', newline='') as result_file:
        writer = csv.writer(result_file)

        with open("input.csv") as file:
            reader = csv.reader(file)

            # next(reader)  # Skip header row

            for name, email in reader:
                try:
                    server.sendmail(
                        sender_email,
                        email,
                        message.as_string()
                    )
                    writer.writerow([email, 'Successful'])
                except:
                    writer.writerow([email, 'Unsuccessful'])

        