import smtplib
from email.message import EmailMessage
import imghdr
import re

# stmp.gmail.com의 서버주소와 포트번호
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    # 유효한 이메일 주소인지 판단하는 '정규표현식'
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("이것은 본문입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "###@gmail.com"
message["To"] = "###@gmail.com"

with open("#file_name#.png","rb") as image:
    image_file = image.read()

# image의 type이 무엇인지 알려주는 imghdr모듈
image_type = imghdr.what('#file_name#',image_file)
# add_attachment() : 텍스트 외의 사진,비디오 등의 파일형식이 섞이면 mix타입이 되는데 그때 해주는 함수
message.add_attachment(image_file,maintype='image',subtype=image_type) 

# gmail은 SSL보안?? 때문에 이렇게 해줘야함.
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("###@gmail.com","#password#")
# 메일을 보내는 sendEmail 함수를 호출해서 실행해보기
sendEmail("###gmailcom")
smtp.quit()