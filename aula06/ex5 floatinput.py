import math

def floatInput(prompt):
    res = float(input(prompt))
    return res


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    while True:
        try:
            v = floatInput("Value? ")
        except ValueError:
            print("Error: Not a float!")      
        else:
            print("v:", v)
            break

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    while True:
        try:
            h = floatInput("Humidity (%)? ")
        except ValueError:
            print("Error: Not a float!")      
        else:
            if 0<=h<=100:
                print("h:", h)
                break
            else:
                print("Error: Value should be in [0, 100]!")
                continue
    

    print("c) Try entering invalid values such as 23C or -274.")
    while True:
        try:
            t = floatInput("Temperature (Celsius)? ")
        except ValueError:
            print("Error: Not a float!")      
        else:
            if -273.15<=t:
                print("t:", t)
                break
            else:
                print("Error: Value should be higher than -273.15!")
                continue

    # d) What happens if you uncomment this?
    #impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    main()
