import speech_recognition as sr

recognize = sr.Recognizer()
#마이크로 입력된 음성불러오기
with sr.Microphone() as source:
    print('말하세요')
    audio = recognize.listen(source)

# 파일로 부터 음성 불러오기 (wav, aiff/aiff-c, flac 가능)
# with sr.AudioFile('sample.wav') as source: 
# audio = recognize.record(source)
    
try:
    text = recognize.recognize_google(audio, language='ko')
    print(text)
    
except sr.UnknownValueError: #음성인식 실패
    print('인식실패')
except sr.RequestError as e: #key오류 or 네트워크오류
    print('요청 실패 : {0}'.format(e))