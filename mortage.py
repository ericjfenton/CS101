# test input function
# years = input("How many years to pay off? ")
# years = int(years)
# print(years)

while True:
    try:
         x = float(input("Please enter a number: "))
         break
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")
         print("Or enter control-C to exit.")

print(x)

#make the input a function, and test other conditions
