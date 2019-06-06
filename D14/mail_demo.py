from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    message = MIMEMultipart()

    text_content = MIMEText('这是一份我们的选课清单', _subtype='plain', _charset='utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    message.attach(text_content)

    with open('test.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)

    smtper = SMTP('smtp.163.com')
    sender = 'antonio_f_p@163.com'
    receivers = ['antonio_f_p@163.com']

    smtper.login(sender, 'Deng1997')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('发送成功'.center(50, '-'))
    

if __name__ == '__main__':
    main()
