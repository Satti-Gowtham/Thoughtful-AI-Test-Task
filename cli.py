import argparse
from sort import sort

def main():
    parser = argparse.ArgumentParser(description="Package Sorter")

    parser.add_argument('width', type=float, help="Width of the package in cm")
    parser.add_argument('height', type=float, help="Height of the package in cm")
    parser.add_argument('length', type=float, help="Length of the package in cm")
    parser.add_argument('mass', type=float, help="Mass of the package in kg")

    args = parser.parse_args()
    result = sort(args.width, args.height, args.length, args.mass)
    
    print(f"The package should be sent to the {result} stack.")

if __name__ == '__main__':
    main()
