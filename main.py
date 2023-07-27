import sys
import datetime
import random
import time


def check_if_type_is_int_or_str(argument: any) -> bool:
    type_of_argument = type(argument)
    if type_of_argument == str or type_of_argument == int:
        return True
    return False


def check_if_isevaluable(argument: int | str) -> bool:
    try:
        eval(str(argument))
        return True
    except NameError:
        return False


def convert_argument_to_int(argument: int | str) -> int:
    if check_if_type_is_int_or_str(argument):
        if check_if_isevaluable(argument):
            correct_number = int(eval(str(argument)))
            return correct_number
    return False


def check_if_positive_number(number: int | str) -> bool:
    if convert_argument_to_int(number):
        number = convert_argument_to_int(number)
        if not number < 0:
            return True
    return False


def check_number_of_arguments() -> bool:
    number_of_arguments = len(sys.argv)
    if not number_of_arguments < 2:
        return True
    return False


def get_number() -> int:
    if check_number_of_arguments():
        argument = sys.argv[-1]
        int_number = convert_argument_to_int(argument)
        if check_if_positive_number(int_number):
            return int_number
    else:
        raise TypeError('Incorrect number of arguments')


def check_if_number_less_0(number: int | str) -> bool:
    number = convert_argument_to_int(number)
    if number > 0:
        return True
    return False


def print_error(exception_type, value, traceback):
    text = ('While running this program appeared one of this problems:\n'
            '1. Program needs value more than 0 to run\n'
            '2. Or you used some special character that is not allowed\n'
            '      (Characters that are allowed: "+ - * / % **")\n'
            '3. Or you may used some text characters (some words)\n'
            '4. Also may not recognized that this program uses only last argument\n'
            '   You should try to run this program again\n'
            '   We believe that this program with your argument will work!\n')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random()/20)


def show_time(number_of_seconds: int | str) -> print:
    if check_if_number_less_0(number_of_seconds):
        if convert_argument_to_int(number_of_seconds):
            number_of_seconds = convert_argument_to_int(number_of_seconds)
            while check_if_number_less_0(number_of_seconds):
                print(f'Your local time is: '
                      f'{datetime.datetime.now().time().hour}:'
                      f'{datetime.datetime.now().time().minute}')
                number_of_seconds -= 1
    else:
        raise ValueError


sys.excepthook = print_error
