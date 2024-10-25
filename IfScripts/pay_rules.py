# In a file named pay_rules.py, create a script to calculate gross pay given the variables 
# pay_rate and hours_worked. If the person works more than 40 hours, pay the 
# overtime hours at 1.5 times the rate of regular hours. 
pay_rate=float(input(("enter payrate")))

hours_worked=float(input(("enter hours worked")))

if (hours_worked>40):
    salary=pay_rate*((40-hours_worked)*2)
else:
    salary=(pay_rate*hours_worked)

print("your salary is" , salary)





# 2. When you are finished, review your script with a colleague. Are your algorithms 
# similar? Do you believe each other’s code will work? 
# 3. Run your script several times with different values for pay_rate and hours_worked and 
# confirm the output is right.  
