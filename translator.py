from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요 코드라이언입니다."
sentence = input("번역을 원하는 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요?")

result = translator.translate(sentence,dest)  #dest=어떤 언어로 번역할건지 ,src=source text 언어 (생략 가능)
detected = translator.detect(sentence)   #언어 감지

print("===========출 력 결 과===========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("=================================")