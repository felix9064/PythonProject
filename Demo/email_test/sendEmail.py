#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用STMP协议发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_address = "zhang1zhi7hua5@163.com"
password = "Felix@1005"
to_address = "zhangzh@sunline.cn"

# SMTP服务器地址
smtp_server = "smtp.163.com"

# 构建一封纯文本邮件
msg = MIMEText("您好，这是一封通过Python程序发送的电子邮件", "plain", "utf-8")
# 发件人
msg['From'] = _format_addr('Felix<%s>' % from_address)
# 收件人
msg['To'] = _format_addr('zhangzh<%s>' % to_address)
# 主题
msg['Subject'] = Header('无题', 'utf-8').encode()

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_address, password)
server.sendmail(from_address, [to_address], msg.as_string())
server.quit()
