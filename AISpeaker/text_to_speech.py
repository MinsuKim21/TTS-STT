# TTS text_to_speech
# STT speech_to_text

from gtts import gTTS

text = 'can i help you?'
file_name = 'sample.mp3'
tts_en = gTTS(text = text, lang='en')
tts_en.save(file_name)