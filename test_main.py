import main
import sys


def test_check_if_correct_type():
    argument_v1 = '65+40/2'
    argument_v2 = 9012345678998765
    argument_v3 = [9092031, 2312412412]
    condition1 = main.check_if_type_is_int_or_str(argument_v1)
    condition2 = main.check_if_type_is_int_or_str(argument_v2)
    condition3 = not main.check_if_type_is_int_or_str(argument_v3)
    list_of_conditions = [condition1, condition2, condition3]
    assert all(list_of_conditions)


def test_convert_sys_argument_to_int():
    argument_v1 = '65+40/2'
    argument_v2 = [9092031, 2312412412]
    condition1 = main.convert_argument_to_int(argument_v1) == 85
    condition2 = not main.convert_argument_to_int(argument_v2)
    list_of_conditions = [condition1, condition2]
    assert all(list_of_conditions)


def test_check_if_positive_number():
    argument_v1 = '65+40/2'
    argument_v2 = [9092031, 2312412412]
    condition1 = main.check_if_positive_number(argument_v1)
    condition2 = not main.check_if_positive_number(argument_v2)


def test_check_number_of_arguments():
    sys.argv = [7688]
    condition1 = not main.check_number_of_arguments()
    sys.argv = [7688, 12331]
    condition2 = main.check_number_of_arguments()
    list_of_conditions = [condition1, condition2]
    assert all(list_of_conditions)


def test_get_number():
    sys.argv = [12380193, '1234/123']
    condition1 = main.get_number() == 10
    sys.argv = ['1234567890', 'asdasajfkjhald']
    try:
        main.get_number()
        condition2 = False
    except NameError:
        condition2 = True
    sys.argv = ['123sdcbnsfad0', [13245, '23456']]
    condition3 = not main.get_number()
    list_of_conditions = [condition1, condition2, condition3]
    assert all(list_of_conditions)


def test_check_if_number_less_0():
    argument_v1 = '1345'
    argument_v2 = 'sdfghjk'
    argument_v3 = {'asdfgfg': 1232,
                   1234: 123456789}
    condition1 = main.check_if_number_less_0(argument_v1)
    try:
        main.check_if_number_less_0(argument_v2)
        condition2 = False
    except NameError:
        condition2 = True
    condition3 = not main.check_if_number_less_0(argument_v3)
    list_of_conditions = [condition1, condition2, condition3]
    assert all(list_of_conditions)





