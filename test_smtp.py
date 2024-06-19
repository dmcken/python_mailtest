

# System imports
import logging
import smtplib

from email.message import EmailMessage

# External imports
import dotenv

logging.basicConfig(
    #filename='example.log',
    # encoding='utf-8',
    level=logging.DEBUG
)

settings = dotenv.dotenv_values()

logging.info("Start")
svr = smtplib.SMTP(
    host=settings['hostname'],
    port=settings['port']
)
svr.set_debuglevel(2)
svr.ehlo()
svr.starttls()

svr.login(
    user     = settings['username'],
    password = settings['password'],
)

test_number = 2
msg = EmailMessage()
msg['From'] = "GD Info <info@greendotgroup.co>"
msg['To'] = "David Mc Ken <david.mcken@gmail.com>"
msg['Subject'] = f'Test e-mail #{test_number}'
msg.set_content(
    f"""
    This is a e-mail test #{test_number}

    Some more lines, lets see if this makes a difference.
    """
)

# send our email message 'msg' to our boss
svr.sendmail(
    from_addr='info@greendotgroup.co',
    to_addrs='david.mcken@codepro.guru',
    msg="Test body #1",
)

svr.quit()  # finally, don't forget to close the connection
logging.info("End")
