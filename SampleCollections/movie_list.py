# Create a list with the titles of your favorite movies (or movies you’d like to watch) – 
# include at least 2, but no more than 10. 
# 3. Use the len() function to print the descriptive statement: 
# The list [list name] includes my top [length] favorite movies 
# (Or: The list [list name] includes the [length] movies I’d like to watch)

list=['gifted hands','gifted']
length=len(list)

print (( 'The list' ,list ,' includes the',str(length) ,' movies I’d like to watch'))


#  Print a sorted list two ways – Note: make sure that your list items aren’t already in 
# alphabetical order to start with!: 
# ∗ Use the sorted() function to print a sorted list, then print the list again without 
# using sorted() 

print(sorted(list))
print(list)

# Use the .sort() method to sort the list, then print the list again, like this:
list.sort()
print(list)


### difference btw sorted and .sort is that sorted just srots the list when outputing while sort() 
# sorts the list in the list changing the list 

# Think of at least one more movie to add to your list, and use the .append() method to 
# add it. Then print the list again, also including an updated description statement. 
list.append('king fu panda')
print(list)