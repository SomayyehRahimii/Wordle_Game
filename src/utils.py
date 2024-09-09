from termcolor import colored

def print_correct(text, end=' '):
    print(colored(text, 'white', 'on_green'), end=end)

def print_warning(text, end=' '):
    print(colored(text, 'black', 'on_yellow'), end=end)

def print_error(text, end=' '):
    print(colored(text, 'white', 'on_red'), end=end)