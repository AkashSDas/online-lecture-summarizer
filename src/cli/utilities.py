from inferences import predict_text
from load_data import decoder_model, encoder_model
from speech_to_text import hear
from text_to_speech import speak


def show_help() -> None:
    print('''
Usage:
  1. Text to Speech
  2. Speech to Text
  3. AI to create summary of the text

Warning:
  1. Be connected to internet to use tts using gtts & stt

Commands:
  help                                                  Show commands and usage
  clear                                                 Clear CLI screen
  exit                                                  Exit
  tts os <filename>                                     Just reads the text from the file
  tts gtts <filename> <audio-filename>                  Reads the text file, can save audio (default: False),
                                                        audio filename (if save-audio = True) (format: .mp3)
  stt <hours> <mins> <save-txt> <filename> <print-txt>  Listen for speech for <hours> hours, <mins> minutes,
                                                        save's it to a file <filename> if <save-txt> is True,
                                                        <print-text> if True will show the text in console
                                                        default: <save-txt>: True, <filename>: transcripit.txt,
                                                        <print-txt>: False

❗ You need to provide a text filename of whose summary you want to make.
AI untility commands
  ai <text-filename> <save-summary-filename>
    ''')


def welcome() -> None:
    print('\n🌈 Text Summariztion CLI (version 1.0.0)\n')
    show_help()


def clear() -> None:
    print('\n' * 40)


# Text to speech command
def run_tts(commands_list: list) -> None:
    commands = {
        'way': commands_list[1],
        'filename': commands_list[2],
    }
    try:
        commands['audio_filename'] = commands_list[3]
    except IndexError:
        commands['audio_filename'] = 'voice.mp3'

    status = speak(commands['filename'], commands['way'],
                   commands['audio_filename'])

    print(status['message'])


# Speect to text command
def run_stt(commands_list: list) -> None:
    try:
        commands = {
            'hours': int(commands_list[1]),
            'minutes': int(commands_list[2]),
        }
        optional_fields = ['save_text', 'filename', 'print_text']
        default_values = [True, 'transcript.txt', False]
        for idx, (option, default_value) in enumerate(zip(optional_fields, default_values)):
            try:
                # [idx + 3]: since first 2 items in the list not optional &
                # first idx = 0
                commands[option] = commands_list[idx + 3]
            except IndexError:
                commands[option] = default_value

        hear(commands['hours'], commands['minutes'], commands['save_text'],
             commands['filename'], commands['print_text'])
    except ValueError:
        print('❌ Invalid hours/minutes')
    except Exception as e:
        print('❌ Invalid command, For help enter "help" without quotes')


# for creating summary
def ai(filename: str, save_filename: str, decode_sequence) -> None:
    with open(filename, 'r') as f:
        text = f.read()
    summary = predict_text(text, decode_sequence, encoder_model, decoder_model)
    with open(save_filename, 'w') as f:
        f.write(str(summary))
    print(f'⭐ Summary: {summary}')
