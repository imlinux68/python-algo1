#! /bin/python

def sum_num():
    a = int(input("Enter a number: "))
    s = 0
    while a > 0:
        s += a % 10
        a = a // 10
    print(s)

if __name__ == "__main__":
    sum_num()
