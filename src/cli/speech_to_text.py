import time

import speech_recognition as sr
from gtts import gTTS


def get_current_time():
    hour, minute = time.localtime()[3], time.localtime()[4]
    return hour, minute


# def listen_once(save_text=True, filename='transcript.txt', print_text=False) -> None:
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         r.energy_threshold = 1000
#         print('👂 Listening...')
#         audio = r.listen(source)

#         try:
#             text = r.recognize_google(audio)
#         except Exception as e:
#             print(f'❌ Not audible')

#     if save_text:
#         with open(filename, 'w') as f:
#             f.write(text)
#     if print_text:
#         print(f'🍩 Text: \n\t{text}')

#     print(f'✅ Transcript saved to {filename}')


def hear(stop_after_hours, stop_after_minutes, save_text=True, filename='transcript.txt', print_text=False) -> None:
    r = sr.Recognizer()
    text = ''

    # when to stop
    current_hour, current_minute = get_current_time()
    stop_hours = current_hour + stop_after_hours
    stop_minutes = current_minute + stop_after_minutes

    # If the person keep's on speaking the current_hour & current_minute
    # will exceed the stop_hour & stop_minute (since the code is awaited in listening),
    # but once the person stop's for a moment & the while loop's condition doesn't holds
    # then the loop will stop.
    while current_hour <= stop_hours and current_minute < stop_minutes:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 800
            print('👂 Listening...')
            audio = r.listen(source)

            try:
                said = r.recognize_google(audio)

                # concatenating text (of audio in current iteration) with main text
                text += said
            except Exception as e:
                print(f'❌ Not audible')

        # getting the current time data
        current_hour, current_minute = get_current_time()

    if save_text:
        with open(filename, 'w') as f:
            f.write(text)
    if print_text:
        print(f'🍩 Text: \n\t{text}')

    print(f'✅ Transcript saved to {filename}')
