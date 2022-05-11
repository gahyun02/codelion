#이메일 정규 표현식: ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$
#조건에 부합하는 이메일 예시: codelion.example@gmail.com
import smtplib
from email.message import EmailMessage 
import imghdr   #이미지 유형 판단
import re  #이메일 유효성 검사

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
	reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
	if bool(re.match(reg,addr)):
		print("정상적으로 메일이 발송되었습니다.")
	else:
		print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage() #MIME형태로 변환시켜줌
message.set_content("코드라이언 수업중입니다.")   #이메일 본문 내용

message["Subject"] = "이것은 제목입니다."
message["From"] = "sunshineonmyneck@gmail.com"
message["To"] = "igh2468@likelion.org"

with open("codelion.png","rb") as image:   #rb는 read binary 모드임. #안전하게 파일 열고 닫는 방법
	image_file = image.read()

image_type = imghdr.what('codelion',image_file)  #파일명, 실제 데이터

#multipart/mixed 타입의 메일의 경우
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("sunshineonmyneck@gmail.com","guccigang")

sendEmail("codelion.example@gmail.com")
smtp.quit()