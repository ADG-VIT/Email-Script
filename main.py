import smtplib, ssl, csv 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from time import sleep

sender_email = input("Type your email and press enter:")
password = input("Type your password and press enter:")

# sender_email = ''
# password = ''

message = MIMEMultipart("alternative")

# ENTER SUBJECT OF MAIL
message["Subject"] = "💥 Urgent: Round 2 of ADG's Recruitment Drive 💥"

message['From'] = formataddr(('Apple Developers Group VIT', sender_email))

# Create secure connection with server and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)

    with open('success.csv', 'w', newline='') as successful_file, open('failure.csv', 'w', newline='') as unsuccessful_file:
        success = csv.writer(successful_file)
        failure = csv.writer(unsuccessful_file)

        with open("shortlisted.csv") as file:
            reader = csv.reader(file)

            # next(reader)  # Skip header row

            count = 0

            for tech, design, management, name, regno, email, phone, githubLink, slot in reader:

                if(count >= 75):
                    sleep(150)
                    count = 0

                count += 1
                
                try:
                    # Create the HTML version of your message
                    html = """
                    <!DOCTYPE html>
                    <html>
                      <head>
                        <title></title>
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                        <style type="text/css">
                          @media screen {
                            @font-face {
                              font-family: "Lato";
                              font-style: normal;
                              font-weight: 400;
                              src: local("Lato Regular"), local("Lato-Regular"),
                                url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff)
                                  format("woff");
                            }

                            @font-face {
                              font-family: "Lato";
                              font-style: normal;
                              font-weight: 700;
                              src: local("Lato Bold"), local("Lato-Bold"),
                                url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff)
                                  format("woff");
                            }

                            @font-face {
                              font-family: "Lato";
                              font-style: italic;
                              font-weight: 400;
                              src: local("Lato Italic"), local("Lato-Italic"),
                                url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff)
                                  format("woff");
                            }

                            @font-face {
                              font-family: "Lato";
                              font-style: italic;
                              font-weight: 700;
                              src: local("Lato Bold Italic"), local("Lato-BoldItalic"),
                                url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff)
                                  format("woff");
                            }
                          }

                          /* CLIENT-SPECIFIC STYLES */
                          .custom {
                            font-weight: bold;
                            color: #027aff;
                          }
                          body,
                          table,
                          td,
                          a {
                            -webkit-text-size-adjust: 100%;
                            -ms-text-size-adjust: 100%;
                          }

                          table,
                          td {
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                          }

                          img {
                            -ms-interpolation-mode: bicubic;
                          }

                          /* RESET STYLES */
                          img {
                            border: 0;
                            height: auto;
                            line-height: 100%;
                            outline: none;
                            text-decoration: none;
                          }

                          table {
                            border-collapse: collapse !important;
                          }

                          body {
                            height: 100% !important;
                            margin: 0 !important;
                            padding: 0 !important;
                            width: 100% !important;
                          }

                          /* iOS BLUE LINKS */
                          a[x-apple-data-detectors] {
                            color: inherit !important;
                            text-decoration: none !important;
                            font-size: inherit !important;
                            font-family: inherit !important;
                            font-weight: inherit !important;
                            line-height: inherit !important;
                          }

                          /* MOBILE STYLES */
                          @media screen and (max-width: 600px) {
                            h1 {
                              font-size: 32px !important;
                              line-height: 32px !important;
                            }
                          }

                          /* ANDROID CENTER FIX */
                          div[style*="margin: 16px 0;"] {
                            margin: 0 !important;
                          }
                        </style>
                      </head>

                      <body
                        style="
                          background-color: #f4f4f4;
                          margin: 0 !important;
                          padding: 0 !important;
                        "
                      >
                        <!-- HIDDEN PREHEADER TEXT -->
                        <table
                          style="margin-bottom: 30px"
                          border="0"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                        >
                          <!-- LOGO -->
                          <tr>
                            <td bgcolor="#191919" align="center">
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="max-width: 800px"
                              >
                                <tr>
                                  <td
                                    align="center"
                                    valign="top"
                                    style="padding: 40px 10px 40px 10px"
                                  ></td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#191919" align="center" style="padding: 0px 10px 0px 10px">
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="max-width: 800px"
                              >
                                <tr>
                                  <td
                                    bgcolor="#ffffff"
                                    align="center"
                                    valign="top"
                                    style="
                                      padding: 40px 20px 20px 20px;
                                      border-radius: 4px 4px 0px 0px;
                                      color: #111111;
                                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                                      font-size: 48px;
                                      font-weight: 400;
                                      letter-spacing: 4px;
                                      line-height: 48px;
                                    "
                                  >
                                    <h1 style="font-size: 48px; font-weight: 400; margin: 2">
                                      Recruitments 2020
                                    </h1>
                                    <img
                                      src="https://raw.githubusercontent.com/ADG-VIT/IosFusion_Website2019/master/assets/ADG_logo_hr.png"
                                      width="80"
                                      height="80"
                                      style="display: block; border: 0px"
                                    />
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px">
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="max-width: 800px"
                              >
                                <tr>
                                  <td
                                    bgcolor="#ffffff"
                                    align="left"
                                    style="
                                      padding: 20px 30px 40px 30px;
                                      color: #666666;
                                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                                      font-size: 18px;
                                      font-weight: 400;
                                      line-height: 25px;
                                    "
                                  >
                                    <p style="margin: 0; text-align: center">
                                      Greetings from Apple Developers Group!.<br />
                                      Congratulations to the Shortlisted ones! Glad you made it so
                                      far.<br /><br />

                                      You aced the prelims, but Round 2 is where you are really
                                      tested. It’s where you get to interact with ADG Core Members
                                      and the Board. It’s where we meet you for the first time. Gear
                                      up for Round 2 of ADG Recruitments 2021: ‘Personal
                                      Interview’.<br /><br />

                                      We are pleased to inform you that, you have qualified for the
                                      final round for
                                      <span class="custom">{}</span> domain(s) of
                                      our recruitment process.<br /><br />

                                      Refer to the slot details below:<br />
                                      Date:<span class="custom">{}</span><br />
                                      Time slot:<span class="custom">{}</span><br />
                                      Discord Server:
                                      <a
                                        href="https://discord.com/invite/NFekVBVMGQ"
                                        target="_blank"
                                        >https://discord.com/invite/NFekVBVMGQ</a
                                      ><br /><br />

                                      We have also attached a very detailed help guide to answer all
                                      your doubts related to Discord. Hence check that out, as well.<br>
                                      All the best!!<br> Be there as we unleash the hidden talent in
                                      you!
                                    </p>

                                    <br />
                                  </td>
                                </tr>
                                <tr>
                                  <td bgcolor="#ffffff" align="left">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                      <tr>
                                        <td
                                          bgcolor="#ffffff"
                                          align="center"
                                          style="padding: 20px 30px 60px 30px"
                                        >
                                          <table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                              <td align="center" style="border-radius: 3px">
                                                <img
                                                  src="https://raw.githubusercontent.com/ADG-VIT/Email-Script/master/round2.png"
                                                  width="500"
                                                  height="500"
                                                  style="display: block; border: 0px"
                                                />
                                              </td>
                                            </tr>
                                          </table>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                                <!-- COPY -->
                                <tr>
                                  <td
                                    bgcolor="#ffffff"
                                    align="left"
                                    style="
                                      padding: 0px 30px 20px 30px;
                                      color: #666666;
                                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                                      font-size: 18px;
                                      font-weight: 400;
                                      line-height: 25px;
                                    "
                                  >
                                    <p style="margin: 0">
                                      Cheers,<br />Team Apple Developers Group
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    bgcolor="#ffffff"
                                    align="left"
                                    style="
                                      padding: 0px 30px 40px 30px;
                                      border-radius: 0px 0px 4px 4px;
                                      color: #666666;
                                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                                      font-size: 12px;
                                      font-weight: 400;
                                    "
                                  >
                                    <p style="margin: 0">
                                      This email was sent from a notification-only address that
                                      cannot accept incoming email. Please do not reply to this
                                      message. <br /><br />Incase of any queries or discrepancies,
                                      please feel free to contact us at:
                                      <a href="mailto:appledevelopersgroup@gmail.com"
                                        >appledevelopersgroup@gmail.com</a
                                      >
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td
                              bgcolor="#f4f4f4"
                              align="center"
                              style="padding: 30px 10px 0px 10px"
                            >
                              <table
                                bgcolor="#191919"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="max-width: 800px; border-radius: 5px"
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="
                                      padding: 30px 30px 30px 30px;
                                      border-radius: 4px 4px 4px 4px;
                                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                                      font-size: 18px;
                                      font-weight: 400;
                                      line-height: 25px;
                                    "
                                  >
                                    <h2
                                      style="
                                        font-size: 20px;
                                        font-weight: 400;
                                        color: #ffff;
                                        margin: 0;
                                      "
                                    >
                                      Need more help?
                                    </h2>
                                    <br />
                                    <a
                                      style="
                                        font-size: 20px;
                                        font-family: Helvetica, Arial, sans-serif;
                                        color: #ffffff;
                                        display: inline-block;
                                      "
                                      href="https://www.facebook.com/vitios/"
                                      target="_blank"
                                      ><img
                                        src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/facebook-logo-min.png"
                                        style="
                                          width: 18px;
                                          height: 18px;
                                          float: left;
                                          overflow: hidden;
                                        "
                                    /></a>
                                    &emsp;
                                    <a
                                      style="
                                        font-size: 20px;
                                        font-family: Helvetica, Arial, sans-serif;
                                        color: #ffffff;
                                        display: inline-block;
                                      "
                                      href="https://www.linkedin.com/company/adgvit/"
                                      target="_blank"
                                      ><img
                                        src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/linkedin-logo-min.png"
                                        style="
                                          width: 18px;
                                          height: 18px;
                                          float: left;
                                          overflow: hidden;
                                        "
                                    /></a>
                                    &emsp;
                                    <a
                                      style="
                                        font-size: 20px;
                                        font-family: Helvetica, Arial, sans-serif;
                                        color: #ffffff;
                                        display: inline-block;
                                      "
                                      href="https://www.instagram.com/adgvit/"
                                      target="_blank"
                                      ><img
                                        src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/instagram-logo-min.png"
                                        style="
                                          width: 18px;
                                          height: 18px;
                                          float: left;
                                          overflow: hidden;
                                        "
                                    /></a>
                                    &emsp;
                                    <a
                                      style="
                                        font-size: 20px;
                                        font-family: Helvetica, Arial, sans-serif;
                                        color: #ffffff;
                                        display: inline-block;
                                      "
                                      href="https://twitter.com/adgvit"
                                      target="_blank"
                                      ><img
                                        src="https://raw.githubusercontent.com/ADG-VIT/ADG-Official-Website-2020/master/commonAssets/imgs/twitter-2-min.png"
                                        style="
                                          width: 18px;
                                          height: 18px;
                                          float: left;
                                          overflow: hidden;
                                        "
                                    /></a>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </body>
                    </html>
                    """
                    # Turn into html MIMEText objects
                    part = MIMEText(html, "html")

                    # Add HTML part to MIMEMultipart message
                    message.attach(part)

                    server.sendmail(
                        sender_email,
                        email,
                        message.as_string()
                    )
                    success.writerow([regno, email, 'Successful'])
                    print(count, 'Successful', email)
                except:
                    failure.writerow([regno, email, 'Unsuccessful'])
                    print(count, 'Unsuccessful', email)
                    sleep(150)
                    count = 0

        