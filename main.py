import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a cell reference as an argument (e.g. A1)")
        return
    
    cell_reference = sys.argv[1]
    # Rest of your code here

if __name__ == '__main__':
    main()
