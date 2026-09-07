
try:
    number = int(input("enter number : "))
    result = 100/number
    print(f"result{result}")

except ValueError:
    print("enter a valid number")

except ZeroDivisionError:
    print("cannot divide by zero")

finally:
    print("program finished")
