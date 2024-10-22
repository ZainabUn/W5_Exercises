# How long will it take a savings account worth X to double in value based on an interest
# rate of IR? (Hint: Look up the rule of 72)

#testing rate of 3
rate=3

#formula
double_value_time= 72/rate

print('At a ' ,format(rate, ".2f") , ' % ', 'interest rate, your savings account will be worth double in', format(double_value_time,".1f"),' number years')