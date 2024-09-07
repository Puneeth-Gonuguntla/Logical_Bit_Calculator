# CS50 Final Project -- LOGICAL BIT CALCULATOR

def main():
    print("1. AND Gate")
    print("2. OR Gate")
    print("3. NOT Gate")
    print("4. NAND Gate")
    print("5. NOR Gate")
    print("6. XOR Gate")
    print("7. XNOR Gate")
    choice = int(input("Enter your choice: "))


    if choice == 3:
        a = binary_value("Enter the Binary input: ")
        print("Result:", NOT(a))

    elif choice in [1,2,4,5,6,7]:
        a = binary_value("Enter the first Binary input: ")
        b = binary_value("Enter the second Binary input: ")
        if choice == 1:
            print("Result:", AND(a, b))
        elif choice == 2:
            print("Result:", OR(a, b))
        elif choice == 4:
            print("Result:", NAND(a, b))
        elif choice == 5:
            print("Result:", NOR(a, b))
        elif choice == 6:
            print("Result:", XOR(a, b))
        elif choice == 7:
            print("Result:", XNOR(a, b))

    else:
        print("Invalid choice")

# Logic Gate AND
def AND(a, b):
    return a and b

# Logic Gate OR
def OR(a, b):
    return a or b

# Logic Gate NOT
def NOT(a):
    return 1 if not a else 0

# Logic Gate NAND
def NAND(a, b):
    return 1 if not (a and b) else 0

# Logic Gate NOR
def NOR(a, b):
    return 1 if not (a or b) else 0

# Logic Gate XOR
def XOR(a, b):
    return 1 if a != b else 0

# Logic Gate XNOR
def XNOR(a, b):
    return 1 if a == b else 0

#For ensuring Input numbers are of Binary Value
def binary_value(value):
    while True:
        try:
            value = int(input(value))
            if value in [0, 1]:
                return value
            else:
                raise ValueError("Input must be 0 or 1.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
