'''
Author: Mohammad Ismail Ashiq Aslam
Task: ASCII Art(Part B)
Name: Saguaro

'''

def main():
    top()
    mid()
    bottom()

def top():
    print("  "+"x"*3+"    "+"x"*6)
    dash = "-----"
    bar = "/"
    for i in range(0,5):
        print(" X---X  "+"X"+bar+dash+"X")
        dash = dash[:-1]
        bar = bar + "/"

def mid():
    print("  xxxxxxX~~~~~~X   xxx")
    dash = "-----"
    bar = " \ "
    for i in range(0,5):
        print("        "+"X"+dash+bar.replace(" ", "")+"X"+"  X---X")
        dash = dash[:-1]
        bar = bar + " \ "

def bottom():
    print("        X~~~~~~Xxxxxxx")
    for i in range(0,6):
        print("        X~~~~~~X")
        

main()
