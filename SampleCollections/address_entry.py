# Create a file named address_entry.py, and in it define a dictionary that includes the 
# following keys and the sample values of your choice: 
# name 
# address 
# city 
# state 
# zip 

adress= {
    'name' : 'Zainab Unisa',
    'address':'1234 Secret Island street',
    'city': 'paradise',
    'state': 'DK',
    'zip':'9876',

}


# 2. Print the address as properly formatted for mailing. Avoid using multiple print 
# statements. Experiment with using a multi-line f-string (triple quotes), or use "\n" (new 
# line) to break the address into multiple lines. 
adress_string=str(adress.values())

print( adress['name']+ " \n"  + adress['address']+ "\n"+ adress['city']+" " + adress['state']+ " "+ adress['zip'] )

# 3. Remove the key:value pair for name.  
adress.pop('name')
print(adress)

# 4. Add a new variable for full_name and assign its value as a tuple containing two 
# key:value pairs. The first key:value pair should contain the key “first name” and a first 
# name, and the second should contain the key “last name” and a last name. 
full_name=  

# 5. Use the .update() method to add one more key:value pair, with the key “honorific” and 
# the value set to Mr. / Ms. / Mx. / Dr. / Hon. / etc. as appropriate. 
# 6. Print the formatted address again, updating as needed to include the new dictionary 
# items.