# change to function format

def calc_payment(years, annual_rate, principal):
    months = 12 * years
    monthly_rate = annual_rate/1200
    # convert from annual percentage to monthly decimal rate
    formula1 = (1 + monthly_rate) ** months
    # print(formula)
    payment = monthly_rate * principal * formula1 / (formula1 - 1)
    return payment

# lines that call function here
years = 20.0
annual_rate = 5.0
principal = 100000.00

payment = calc_payment(years, annual_rate, principal)
print(payment)



