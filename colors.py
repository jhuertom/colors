import sys
from datetime import datetime

printalias = print

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print(msg):
    printalias(f"{bcolors.OKGREEN}{datetime.now()}{bcolors.HEADER} --> {bcolors.OKBLUE}{msg}{bcolors.ENDC}", file=sys.stdout)

def warn(msg):
    printalias(f"{bcolors.OKGREEN}{datetime.now()}{bcolors.HEADER} --> {bcolors.WARNING}{msg}{bcolors.ENDC}", file=sys.stdout)

def err(msg):
    printalias(f"{bcolors.OKGREEN}{datetime.now()}{bcolors.HEADER} --> {bcolors.FAIL}{bcolors.BOLD}{msg}{bcolors.ENDC}", file=sys.stderr)
