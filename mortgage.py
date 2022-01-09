# copy the two checking functions here and test combined version

def verify_input(question):
    while True:
        try:
             x = float(input(question))
             break
        except ValueError:
             print("Not a valid number. Try again or enter control-C to exit.")
    return x

def check_it(x, rangelow,  rangehi):
    if x >= rangelow and x <= rangehi:
        return True
    else:
        return False

def calc_payment(years, annual_rate, principal):
    months = 12 * years
    monthly_rate = annual_rate/1200
    # convert from annual percentage to monthly decimal rate
    formula1 = (1 + monthly_rate) ** months
    # print(formula)
    payment = monthly_rate * principal * formula1 / (formula1 - 1)
    return payment

# get years to pay off

rangelow = 1.0
rangehi = 30.0
myflag = False
question = "Enter years to pay off (1.0 to 30.0): "
while myflag == False:
    years = verify_input(question)
    myflag = check_it(years, rangelow,  rangehi)

# get annual interest rate

rangelow = 1.0
rangehi = 12.0
myflag = False
question = "Enter annual interest rate (1.0 to 12.0): "
while myflag == False:
    annual_rate = verify_input(question)
    myflag = check_it(annual_rate, rangelow,  rangehi)

# get principal

rangelow = 100.0
rangehi = 1000000000.0
myflag = False
question = "Enter principal (no punctuation, one hundred to one million): "
while myflag == False:
    principal = verify_input(question)
    myflag = check_it(principal, rangelow,  rangehi)

payment = calc_payment(years, annual_rate, principal)
print("Monthly payment is $" + str(payment))

    
