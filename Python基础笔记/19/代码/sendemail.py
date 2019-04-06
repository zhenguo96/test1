# 发送邮件
import smtplib
from email.header import Header
from email.mime.text import MIMEText

class Emailer:
    def __init__(self,user,password,host):
        """
        
        :param user: 用户名 
        :param password: 授权码
        :param host: 邮件服务器地址
        """
        self.user = user
        self.password = password
        self.host = host
    def send(self,sender,revicer,content,title):
        pass
    















