import sys
import os
import re
import getpass
import functools


def load_blacklist(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        return [line.strip() for line in file_handler]


def calc_rating_length(password):
    if len(password) > 10:
        return 10
    return len(password)


def calc_rating_strength(password):
    check_regexp = [r'\d', r'[a-z]', r'[A-Z]', r'\W']
    check_regexp = list(map(lambda r: re.search(r, password) is not None, check_regexp))
    count_positive_checks = functools.reduce(lambda x, y: x + y, check_regexp)
    return count_positive_checks / len(check_regexp)


def get_password_strength(password, path_to_blacklist=None):
    blacklist = None
    if path_to_blacklist:
        blacklist = load_blacklist(path_to_blacklist)
    if blacklist and password in blacklist:
        return 1
    return round(calc_rating_length(password)*calc_rating_strength(password))


def print_password_strength(strength):
    print('Your password strength is {0}'.format(strength))


if __name__ == '__main__':
    blacklist_filepath = None
    if len(sys.argv) > 1:
        blacklist_filepath = sys.argv[1]
    password = getpass.getpass()
    password_strength = get_password_strength(password, blacklist_filepath)
    print_password_strength(password_strength)
