#  Create a script named min_max.py that displays both the smallest and then the 
# largest of three numbers. 
# Name your variables a, b, and c and assign them values. Then use if/else statements 
# to determine and display the answer. 
# Be sure to test your script using an assortment of different values in your variables, so 
# that you look at a variety of different number combinations.

a=8;
b=8;
c=8;

if a<b and a<c:
    "a is greater"
elif b<a and b<c:
    "b is greater"
elif c<a and c<b:
    "c is greater"
# elif a==b or 
else:
    print('check input again. ')
