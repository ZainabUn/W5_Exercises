# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?
# Code the script in a file named rentals.py
# Test your script with 38 tourists. Now do some calculations by hand to check your
# work.
# ∗ How much money did your script say you had to charge per person?
# ∗ If you multiply that out, how much did you collect?
# ∗ How much were the vans?
# ∗ Why do you have leftover money?
import math
def trip(people):
    driverspay=0
    vans= math.ceil(people/15)
    totalcost=(vans*250)+driverspay
    costfor15=(250+driverspay)/15
    costperperson= (totalcost)/(people)

    return costperperson

print('cost per person is $',round(trip(38),2))


#trying in class 10/23
var= "house"
print(var[-5:0])
#negative to positive does not seem to work

