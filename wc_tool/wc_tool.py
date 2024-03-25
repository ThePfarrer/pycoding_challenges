import os.path
import sys


def number_of_bytes(file):
    return os.path.getsize(file)


def number_of_lines(file):
    with open(file) as text_file:
        lines = text_file.readlines()

    return len(lines)


def number_of_words(file):
    with open(file) as text_file:
        words = text_file.read().split()

    return len(words)


def number_of_characters(file):
    with open(file) as text_file:
        characters = list(text_file.read())

    return len(characters)

def no_flag(file):
    lines = number_of_lines(file)
    words = number_of_words(file)
    bytes = number_of_bytes(file)

    return lines, words, bytes, file

n = len(sys.argv)

valid_flags = {'-c': number_of_bytes,
               '-l': number_of_lines,
               '-w': number_of_words,
               '-m': number_of_characters}

if n > 2:
    flag = sys.argv[1]
    file_name = sys.argv[2]
elif n == 2:
    flag = ''
    file_name = sys.argv[1]

    print(str(no_flag(file_name))[1:-1])
    sys.exit()
else:
    sys.exit("Insufficient parameters")

if flag in valid_flags:
    print(valid_flags[flag](file_name), file_name)
else:
    print("Invalid parameters")
