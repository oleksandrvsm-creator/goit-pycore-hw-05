from datetime import datetime


def parse_log_line() -> dict:
    with open('log_file.txt', 'r', encoding='utf-8') as file:
        dict = {'Date': '', 'Time': '', 'Level': '', 'Message': ''}
        for line in file.readlines():
            symbols = line.split()

    return symbols
print(parse_log_line())

