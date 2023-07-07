import configparser
from pathlib import Path

cfg_file = "positive_login.ini"
cfg_file_dir = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfg_file_dir).joinpath(cfg_file)

config.read(CONFIG_FILE)


def get_correct_username():
    return config['login']['username']


def get_correct_password():
    return config['login']['password']


def get_logged_in_page_header():
    return config['login']['logged_in_msg']


if __name__ == "__main__":
    print(get_correct_username())
    print(get_correct_password())
    print(get_logged_in_page_header())
