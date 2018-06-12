import sys, os, subprocess

values = ["sensitivity", "speed", "inertia"]
maxspace = 0

def inputInRange(p, min, max):
    while True:
        try:
            x = int(input(p))
            if x >= min and x < max:
                return x
            print("Number out of range")
        except ValueError:
            print("Type a number")


def makeSpace():
    leng = 0
    for i in values:
        if len(i) > leng:
            leng = len(i)
    return len(i)+5

def spaced(s):
    global maxspace
    return s+(" "*(maxspace-len(s)))

def main():
    global maxspace
    maxspace = makeSpace()
    args = sys.argv[1:]
    name = sys.argv[0]
    name = name[:name.index(".")]
    if len(args) == 0:
        print("Usage:\nsudo "+name+" <sensitivity> <speed> <inertia>\n\n\n")
        sys.exit(0)
    elif not len(args) == len(values):
        print("This script takes 3 arguments")
        sys.exit(1)
    for i in range(len(args)):
        f = open("/sys/devices/platform/i8042/serio1/serio2/"+values[i], "w")
        f.write(args[i])
        f.close()
    print("\nValues written:")
    for i in range(len(args)):
        f = open("/sys/devices/platform/i8042/serio1/serio2/"+values[i], "r")
        print(spaced(values[i])+": "+f.readlines()[0], end="")


if __name__ == "__main__":
    main()
