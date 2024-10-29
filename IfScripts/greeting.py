# Create a script named greeting.py. Define a variable that contains the current hour (0
# 23). Display one of the greetings below based on the current hour: 
# Time 
# until 10:00am 
# 10:00am until 5:00pm 
# 5:00pm or later 
# Greeting 
# Good morning! 
# Good day! 
# Good evening! 
# Remember to test your script several times using different values for the hour. 


##### change it after wards so that user can input am pm and the standard time
# time=12
# time=19
time=9

if 6<time<10:
    print('Good Morning!')
elif 10<= time <17:
    print('Good evening!')
elif time<17:
    print('Good day!')
elif 0 <time< 6  and 
else:
    print('Hi, check input again')

# Update your script to include an additional condition that will print “What are you 
# doing up so late??” if the hour is between 11pm and 4am.