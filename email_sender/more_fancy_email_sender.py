import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
sender_email = input("Enter your address: ")  # "mladentestov@gmail.com"
receiver_email = input("Enter receiver address: ")  # mladentestov@gmail.com
password = input("Enter your password: ")  # mladentestov123

message = MIMEMultipart("alternative")
message["Subject"] = "Choose Your Country"
message["From"] = sender_email
message["To"] = receiver_email

html = """\
<!DOCTYPE html>
<html>
    <head>
        <style >
            body{
                background-color: linen;
            }
            p{
                color: maroon;
            }
            form{
                color:maroon;
            }
            h3{
                color: navy;
            }
        </style>
    </head>
<body>
    <p>Click to choose your country</p>
<form>
<label for="Bulgaria">Bulgaria</label>
<input type="radio" name="country" id="Bulgaria" value="Bulgaria"> <br>
<label for="USA">USA</label>
<input type="radio" name="country" id="USA" value="USA"> <br>
<label for="England">England</label>
<input type="radio" name="country" id="England" value="England"><br>
<label for="Germany">Germany</label>
<input type="radio" name="country" id="Germany" value="Germany"><br>
<label for="France">France</label>
<input type="radio" name="country" id="France" value="France"><br>	
</form> 
</body>
</html>

"""

# Turn these into html MIMEText objects
part = MIMEText(html, "html")

# Add HTML part to MIMEMultipart message
message.attach(part)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    print("E-mail sent!")
