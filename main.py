import smtplib, ssl, csv 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

sender_email = input("Type your email and press enter:")
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")

# ENTER SUBJECT OF MAIL
message["Subject"] = "Christmas Surprise 🎅 🎄"

message['From'] = formataddr(('Apple Developers Group VIT', sender_email))

# Create the HTML version of your message
html = """\
<html>
  <body>
  
    <h2>Sending you something to go fa la la about 🎁</h2>
    <h3 style="font-weight:normal;"> We at <b>Apple Developers Group</b> are proud to announce the launch of our first of its kind mobile application.
    <b>ADG-VIT</b> is an application build to give an insight of what this community holds for you. It is a one stop app for new recruitments, events, projects, FAQs related to various domains and a lot more!
    Download the app now and be prepared for a journey that will cover all your expectations and take you to the unexplored realm of possibilities.
    <br>
    <br>
    The ADG-VIT app is available on both <b>App Store</b> as well as the <b>Play Store.</b></h4>
    <br>
    <br>
    <b>iOS: 📱</b> https://apps.apple.com/in/app/adg-vit/id1545733138
    <br>
    <b>Android: 📱</b> https://play.google.com/store/apps/details?id=com.adgvit.externals 
    <br>
    <br>
    <br>
    <center><img height="500px" width=500px" src="https://raw.githubusercontent.com/ADG-VIT/Email-Script/master/app_launch.png"></center>
    <br>
    <br>
    <br>
    <div style="background-color:#191919; color: white; padding-bottom: 10px; padding-top: 10px; padding-left: 10px; padding-right: 10px; border-radius: 5px;">
        <center><img height="30px" src="https://raw.githubusercontent.com/ADG-VIT/Email-Script/master/adglogo.png"></center>
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

        with open("Apple Developers Group.csv") as file:
            reader = csv.reader(file)

            # next(reader)  # Skip header row

            for regno, email in reader:
                try:
                    server.sendmail(
                        sender_email,
                        email,
                        message.as_string()
                    )
                    writer.writerow([regno, email, 'Successful'])
                    print('Successful')
                except:
                    writer.writerow([regno, email, 'Unsuccessful'])
                    print('Unsuccessful')

        