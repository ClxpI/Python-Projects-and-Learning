'''
Author: Mohammad Ismail Ashiq Aslam
Task: ASCII Art(Part A)
Name: Monitor

'''

def main():
    vertical()
    horizontal()
    vertical()
    stand()


def vertical():
    print("----------------------------------------")

def horizontal():
    for i in range (1,5):
        print("|                                      |\n")

def stand():
    print("             ----|    |---")
    for i in range(1,3):
        print("            |             |")
    print("             -------------")

main()
