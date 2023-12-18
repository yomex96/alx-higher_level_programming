#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    rnums = 0
    for i in range(rnums, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            rnums += 1
        except (ValueError, TypeError):
            pass
    print()
    return rnums
