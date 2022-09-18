import time, os
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound

#음성인식
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[사용자] '+ text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패 :{0}'.format(e))

#대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요 반갑습니다'
    elif '날씨' in input_text:
        answer_text = '덥습니다'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요'
    elif '종료' in input_text:
        answer_text = '다음에 만나요'
        stop_listening(wait_for_stop=False) #실행종료
    else:
        answer_text = '다시 말씀해주시겠어요?'
    speak(answer_text)
    
#텍스트 읽기
def speak(text):
    print('[스피커] '+text)
    file_name = "voice.mp3"
    tts = gTTS(text = text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): #voice.mp3 파일 삭제
        os.remove(file_name)

r = sr.Recognizer()
mic = sr.Microphone()

speak("무엇을 도와드릴까요?")

stop_listening = r.listen_in_background(mic, listen)


while True:
    time.sleep(0.1)