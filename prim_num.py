#! /bin/bash/python


def prim_num():
    a = int(input("Enter a number: "))
    k = 0
    for i in range(1, a+1):
        if a % i == 0:
            k += 1

    if k == 2:
        print("Number is primary!!!")
    else:
        print("Number isn't a primary")


prim_num()
