#!/usr/bin/python3
for fst_number in range(0, 10):
    for scnd_number in range(fst_number + 1, 10):
        if fst_number == 8 and scnd_number == 9:
            print("{}{}".format(fst_number, scnd_number))
        else:
            print("{}{},".format(fst_number, scnd_number), end='')
