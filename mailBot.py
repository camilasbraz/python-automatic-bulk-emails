# -*- coding: utf-8 -*-

# Sometimes, the number of emails that can be sent is limited by the server, so, depending on the number of emails you
# are pllaning to send, it is interesting to have an status column that changes when the email is sent!


# You have to set a google app password
# Follow the instructions on
# https://support.google.com/accounts/answer/185833


# If ssl doesn`t work as expected, do this on terminal (mac):
# open /Applications/Python\ 3.7/Install\ Certificates.command
# pip install --upgrade certifi
# https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import pandas as pd

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
login = ""
password = ''
sender = ""
# cc_aux = ["", ""]
# cc = ','.join(cc_aux)

context = ssl.create_default_context()

server = smtplib.SMTP(smtp_server, port)


# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(login, password)
    with open("test.csv") as file:
        reader = pd.read_csv(file)
        reader_filtro = reader[(reader.statusResposta == "nao respondeu")]
        for index, row in reader_filtro.iterrows():
          message = MIMEMultipart("related")
          message["Subject"] = "Email subjetc"
          message["From"] = sender
          # message["Cc"] = cc
          message["To"] = row['email']
          content = """\
                        <html>

                            <body>

                              <p>Hello {name}, how are you<br><br>
                              
                              This is just a mock email!!<br>
                              
                              Your favorite animal is {fav_aninal}
                              

                            </body>
                          </html>
                          """.format(nome=row['Name'], fav_animal=row['FavAnimal'])

          msg = MIMEText(content, "html")

          message.attach(msg)
          server.send_message(
              message
          )

          del message

          print(f'Sent to {row["email"]}')

