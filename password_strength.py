import sys
import os
import re
import getpass


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
    rating = 0
    delta_rating = 0.25
    if re.search(r'\d', password):
        rating += delta_rating
    if re.search(r'[a-z]', password):
        rating += delta_rating
    if re.search(r'[A-Z]', password):
        rating += delta_rating
    if re.search(r'\W+', password):
        rating += delta_rating
    return rating


def get_password_strength(password, path_to_blacklist=None):
    blacklist = None
    if path_to_blacklist:
        blacklist = load_blacklist(path_to_blacklist)
    if blacklist and password in blacklist:
        return 1
    return round(calc_rating_length(password)*calc_rating_strength(password))


if __name__ == '__main__':
    blacklist_filepath = None
    if len(sys.argv) > 1:
        blacklist_filepath = sys.argv[1]
    password = getpass.getpass()
    print(get_password_strength(password, blacklist_filepath))
