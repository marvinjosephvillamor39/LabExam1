#Problem 1

def gdc_recursive(a,b):
    if b == 0:
        return a
    return gdc_recursive(b, a % b)

def lcm_recursive(a, b):
    return abs(a * b) // gdc_recursive(a, b)
while True:
    try:
        x = int(input("Enter a value for x: "))
        y = int(input("Enter a value for y: "))
        if x <=  0 or y <= 0:
            print("Error: Please inter only postive number!")
            continue
        lcm = lcm_recursive(x, y)
        print(f"The LCM of {x} and {y} is = {lcm}")
        break
    except ValueError:
        print("Invalid: Please integer only Po.")