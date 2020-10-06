import utilities
from inferences import decode_sequence_for_basic_seq2seq_model


def run_command(user_input: str) -> bool:
    try:
        commands_list = user_input.split()
        if commands_list == []:
            pass
        else:
            what_to_do = commands_list[0]
            if what_to_do == 'help':
                utilities.show_help()
            elif what_to_do == 'clear':
                utilities.clear()
            elif what_to_do == 'exit':
                return True
            elif what_to_do == 'tts':
                utilities.run_tts(commands_list)
            elif what_to_do == 'stt':
                utilities.run_stt(commands_list)
            elif what_to_do == 'ai':
                utilities.ai(
                    commands_list[1], commands_list[2], decode_sequence_for_basic_seq2seq_model)
            else:
                print('❌ Invalid command, For help enter "help" without quotes')
    except Exception as e:
        print(e)
        print('❌ Invalid command, For help enter "help" without quotes')

    return False


def listen_for_input() -> str:
    return input('👉 ')


def main() -> None:
    utilities.welcome()
    stop = False
    while not stop:
        try:
            user_input = listen_for_input()
            stop = run_command(user_input)
        except Exception as e:
            print(f'❌ Exception: \n{e}')


if __name__ == '__main__':
    main()
