# concept for checking input:
# set a flag to false
# 2 checks: valid number and in range
# if ok set flag to true and return number

#this function checks range only

def check_it(x, rangelow,  rangehi):
    if x >= rangelow and x <= rangehi:
        return True
    else:
        return False

#test the function

x = 13.0
rangelow = 1.0
rangehi = 12.0

number_ok = check_it(x, rangelow,  rangehi)
print(number_ok)
