import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup


def send_email(title: str) -> None:
    from_addr = "kirino1103@gmail.com"
    to_addr = "joungdongsub@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ", ".join(to_addr)
    msg['Subject'] = title
    body= "일자리 사업 공고 올라옴"
    msg.attach(MIMEText(body, 'plain'))~~

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo(~~
    server.starttls()
    server.login(from_addr, "1234567890")
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

    return;

def crolling_job() -> list:
    url= 'https://www.inje.go.kr/portal/adm/bulletin'
    response = requests.get(url,verify=False)
    html_data = BeautifulSoup(response.text, 'html.parser') 
    program_names = html_data.select('td > a')

    body_array= []
    for tag in program_names:
        body_array.append(tag.get_text())

    return body_array


#  init
crolling_body= crolling_job()
print(crolling_body)

if crolling_body.find("일자리") != -1:
    title= "일자리 사업 공고 올라옴"
    send_email(title)
else:
    /"일자리 사업 공고 없음"
    continue