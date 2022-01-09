# test input function

def verify_input(question):
    while True:
        try:
             x = float(input(question))
             break
        except ValueError:
             print("Not a valid number. Try again or enter control-C to exit.")
    return x

question = "Enter number: "
entry = verify_input(question)
print(entry)

#check other conditions
