"""
Filename: factorial_calculator.py
Author: <Givens,CJ>
Created: <DATE>
Instructor: Holtslander
"""

def factorial():
    print("Enter a whole number on the line below.")
    
    num = int(input())
    
    if num == 0:
        print("0! = 1")
        return

    total = 1
    print(str(num) + "! =", end=" ")

    for i in range(num, 0, -1):
        total = total * i
        print(i, end="")
        if i != 1:
            print(" * ", end="")

    print(" =", total)



# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()
