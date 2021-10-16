import re
import errno
import os


def read_template(game_file):
    """
    A function that will open the file using the file path and read it. And return the text inside the file. if the file path was wrong it will return an error.
    """
    try:
        with open(game_file) as file:
            file_content = file.read()
            return file_content
    except:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), game_file)


def parse_template(text):
    """
    A function that will take the text from the previous one and analyze it. It will put anything inside the curly brackets in a tuple and remove it from the text.
    """
    parse_text = re.findall(r'\{(.*?)\}', text)
    for i in parse_text:
        text = str(text).replace((i), "", 1)
    return text, tuple(parse_text)


def merge(text, parse_text):
    """
    A function that will merge the user inputs with the text by using the format method.
    """
    new_text = str(text).format(*parse_text)
    with open('../assets/test.txt', 'w') as output:
        output.write(new_text)
    return new_text


def game():
    """
    A function that will run the game, print a welcoming message and return the formatted text based on the user inputs.
    """
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
