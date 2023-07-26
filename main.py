import sys
import datetime


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


def show_time(number_of_seconds: int | str) -> print:
    if check_if_number_less_0(number_of_seconds):
        if convert_argument_to_int(number_of_seconds):
            number_of_seconds = convert_argument_to_int(number_of_seconds)
            while check_if_number_less_0(number_of_seconds):
                print(f'{datetime.datetime.now().time().hour}:'
                      f'{datetime.datetime.now().time().minute}')
                number_of_seconds -= 1
    else:
        raise ValueError('Program needs value more than 0 to run')


# number_of_seconds = get_number()
# show_time(number_of_seconds)
