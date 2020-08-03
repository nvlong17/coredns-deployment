#!/usr/bin/python3

import sys
from CoreDNS import *

if __name__ == "__main__":
    case = int(sys.argv[1])
    if case == 1:
        generate_corefile()
    elif case == 2:
        update_corefile()