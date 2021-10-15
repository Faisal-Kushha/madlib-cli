import re
import errno
import os


def read_template(game_file):
    try:
        with open(game_file) as file:
            file_content = file.read()
            return file_content
    except:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), game_file)


def parse_template(text):
    parse_text = re.findall(r'\{(.*?)\}', text)
    for i in parse_text:
        text = text.replace((i), "", 1)
    return text, tuple(parse_text)


def merge(text, parse_text):
    new_text = text.format(*parse_text)
    with open('../assets/test.txt', 'w') as output:
        output.write(new_text)
    return new_text


def game():
    print("###########################################")
    print("Welcome to the Madlib game")
    print(" In the Madlib game you have to enter some answers that will be used in the game, and it will return to you a phrase that contain all your answers in a funny way.")
    print("###########################################")

    x = read_template('../assets/main_text.txt')
    text, parse_text = parse_template(x)
    input2 = []
    for i in parse_text:
        user_input = input(f'Please enter {i}\n')
        input2.append(user_input)
    result = merge(text, input2)
    print("###########################################")
    print(f'\n{result}')


if __name__ == '__main__':
    game()
