import math
import matplotlib.pyplot as plt
import numpy as np
from msvcrt import getch
import os
clear = lambda: os.system('cls')
def AcceptKeyPress(selective=True): #returns string
    key = ord(getch())
    if selective:
        if key == 27:
            return 'ESC'
        elif key == 13:
            return 'ENTER'
        elif key == 224: #Special keys
            key = ord(getch())
            if key == 80:
                return 'DOWN'
            elif key == 72:
                return 'UP'
        else:
            return AcceptKeyPress() #Asks again
def AcceptChoice(header,choices):
    pos = 0
    while True:
        clear()
        print(header)
        for x in choices[:pos]:
            print(x)
        print("> %s " % choices[pos])
        for x in choices[pos+1:]:
            print(x)

        key = AcceptKeyPress()
        if key == 'UP':
            pos -= 1
            if pos < 0:
                pos = len(choices) - 1
        elif key == 'DOWN':
            pos += 1
            if pos > len(choices) - 1:
                pos = 0
        elif key == 'ENTER':
            return pos
class Answer:
    def __init__(self,num,nps,npsr,tv,sv,dif):
        self.num = num
        self.nps = nps
        self.npsr = npsr
        self.tv = tv
        self.sv = sv
        self.dif = dif
############################## START
def CalculateLoss(num):
    if num >= 0:
        offset = 0
        mult = 1
        while math.sqrt(float(num + offset)) % 1 != 0:
            mult = -1
            if math.sqrt(float(num - offset)) % 1 != 0:
                mult = 1
                offset += 1
            else:
                break
        offset *= mult
        nearestPerfectSquare = num + offset
        nearestPerfectSquareRoot = math.sqrt(num + offset)
        theoreticalValue = math.sqrt(num)
        if nearestPerfectSquareRoot == 0:
            shortcutValue = float(0)
        else:
            shortcutValue = nearestPerfectSquareRoot - offset / (nearestPerfectSquareRoot * 2)
        difference = shortcutValue - theoreticalValue
        return Answer(num,nearestPerfectSquare,nearestPerfectSquareRoot,theoreticalValue,shortcutValue,difference)
    else:
        return 'Get real! (Press any button to try again.)'
        AcceptKeyPress(False)
############################ END

def FindRelativeMaximum(x,y):
    newx = []
    newy = []
    for pos in range(0,len(x)-1):
        leftSlope = (y[pos-1] - y[pos]) / (x[pos-1] - x[pos])
        rightSlope = (y[pos] - y[pos+1]) / (x[pos] - x[pos+1]) #Can throw float division by zero error
        if (np.sign(leftSlope) == 1. and np.sign(rightSlope) == -1.):
            newx.append(x[pos])
            newy.append(y[pos])
    return newx, newy

def FindRelativeMinimum(x,y):
    newx = []
    newy = []
    for pos in range(0,len(x)-1):
        leftSlope = (y[pos-1] - y[pos]) / (x[pos-1] - x[pos])
        rightSlope = (y[pos] - y[pos+1]) / (x[pos] - x[pos+1])
        if (np.sign(leftSlope) == -1. and np.sign(rightSlope) == 1.):
            newx.append(x[pos])
            newy.append(y[pos])
    return newx, newy

def Analyze(num = None):
    number = num or input("Enter non-negative integer: ")
    try:
        number = int(number)
    except:
        clear()
        Analyze()
    clear()
    print("%s checks out fine" % number)
    answer = CalculateLoss(number)
    if answer == 'Get real! (Press any button to try again.)':
        Analyze()
    else:
        print("Original number: %d" % int(answer.num))
        print("Nearest perfect square: %d" % int(answer.nps))
        print("Nearest perfect square root: %d" % int(answer.npsr))
        print("Theoretical value: %f" % answer.tv)
        print("Shortcut value: %f" % answer.sv)
        print("Difference: %f" % answer.dif)
        print("Press any key to return to the menu.")
        AcceptKeyPress(False)
        Main()

def Graph(array=None,min=None,max=None):
    if array:
        xarray = array
    else: 
        minimum = min or input("Enter non-negative minimum: ")
        try:
            if (int(minimum) < 0):
                clear()
                Graph()
        except:
            clear()
            Graph()
        maximum = max or input("Enter non-negative maximum (greater than %d)" % int(minimum))
        try:
            if (int(maximum) < int(minimum)):
                clear()
                Graph(min=minimum)
        except:
            clear()
            Graph(min=minimum)
        xarray = range(int(minimum),int(maximum))
    yarray = [CalculateLoss(x).dif for x in xarray]
    maxxarray, maxyarray = FindRelativeMaximum(xarray,yarray)
    minxarray, minyarray = FindRelativeMinimum(xarray,yarray)
    difLine, = plt.plot(xarray,yarray)
    difLine.set_label('Difference')
    maxLine, = plt.plot(maxxarray,maxyarray)
    maxLine.set_label('Relative maximums')
    minLine, = plt.plot(minxarray, minyarray)
    minLine.set_label('Relative minimums')
    plt.legend()
    plt.title('Square Root Shortcutting Inaccuracy')
    plt.ylabel('Difference')
    plt.xlabel('sqrt(number)')
    plt.show()
    print("Press any key to return to the menu.")
    AcceptKeyPress(False)
    Main()

def Main():
    choice = AcceptChoice("Square root shortcut\n(Press enter to select.)",["Analyze square root of single number","Graph range of numbers","Exit"])
    if choice == 0:
        clear()
        Analyze()
    elif choice == 1:
        clear()
        Graph()
    else:
        os._exit(0)
Main()

