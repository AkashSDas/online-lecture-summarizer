from os import system

import playsound
from gtts import gTTS


def speak_text_os(text: str) -> None:
    system(f'say {text}')


def speak_text_gtts(text: str, audio_filename='voice.mp3') -> None:
    tts = gTTS(text=text, lang='en')
    tts.save(audio_filename)
    playsound.playsound(audio_filename)


def speak(filename: str, way: str, audio_filename='voice.mp3') -> dict:
    status = {'success': False, 'error': False, 'message': ''}
    try:
        with open(filename, 'r') as f:
            text = f.read()

        if way == 'gtts':
            speak_text_gtts(text, audio_filename)
        else:
            # use os as last option
            speak_text_os(text)

        status['success'] = True
        status['error'] = False
        status['message'] = '✅ Text read successfully'
        return status
    except FileNotFoundError:
        status['success'] = False
        status['error'] = True
        status['message'] = '❌ File not found'
        return status


# speak_text_os('Hello World')
# speak_text_gtts('Hello World')

# print(speak('tmp.txt', 'gtts'))
