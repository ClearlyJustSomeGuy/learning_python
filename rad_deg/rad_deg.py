from math import pi

def main():
    rad = float(input("Please provide angle in radians: "))
    while rad > 2 * pi:
        rad = rad - 2 * pi
    print(f"{rad:.2f} radians is equal to {convert(rad):.2f} degrees")

def convert(rad):
    return rad * (180 / pi)
    
    
if __name__ == "__main__":
    main()