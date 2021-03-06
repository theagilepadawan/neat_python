# coding=utf-8
import shutil
from colorama import Fore, Back, Style
import datetime

colors = {
    None: Fore.YELLOW,
    "msg": Fore.BLUE,
    "error": Fore.RED,
}
debug = 0


def log_wrapper(func):
    def wrapped_with_log(*args, **kwargs):
        shim_print(func.__name__)
        return func(*args, **kwargs)
    return wrapped_with_log


def shim_print(main_msg, additional_msg="",  level=None):
    """
Utility function used for printing / debugging
    :param main_msg:
    :param additional_msg:
    :param level:
    """
    if not debug and not level:
        return

    cols, rows = shutil.get_terminal_size()
    stars = round((cols - len(" NEAT PYTHON SHIM ")) / 2)
    minusen = False

    starsRight = "*" * stars
    if (stars * 2) + len(" NEAT PYTHON SHIM ") > cols:
        starsRight = "*" * (stars - 1)


    color = colors[level]
    print(color)
    print(f'{"*" * stars} NEAT PYTHON SHIM {starsRight}')
    print()
    print(f"🐍 ({datetime.datetime.now()}) - [{main_msg}{Fore.RESET}{color}]")
    if additional_msg:
        print(f'{Fore.LIGHTMAGENTA_EX}{additional_msg}{Fore.RESET}{color}')
    print()
    print("*" * cols)
    print(Fore.RESET)
    #mport time; time.sleep(5)
