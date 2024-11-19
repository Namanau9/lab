#5.	Write a python program to create a tuple of any five fruits and print. Perform the following tasks:
#i.	Convert the tuple into list and Add a new fruit
#ii.	Create another list of berries and merge both the lists
#iii.	Convert the updated list back into tuple
#iv.	Print the tuple in sorted manner
#v.	Find the index of a particular fruit in a tuple

   # Step 1: Create a tuple of five fruits
fruits = ('apple', 'banana', 'orange', 'grape', 'kiwi')
print("Original tuple of fruits:", fruits)
    # Step 2: Convert the tuple into a list and add a new fruit
fruits_list = list(fruits)
fruits_list.append('mango')
print("List after adding a new fruit:", fruits_list)
   # Step 3: Create another list of berries and merge both lists
berries = ['strawberry', 'blueberry', 'raspberry']
merged_list = fruits_list + berries
print("Merged list of fruits and berries:", merged_list)
   # Step 4: Convert the updated list back into a tuple
merged_tuple = tuple(merged_list)
print("Updated tuple:", merged_tuple)
   # Step 5: Print the tuple in sorted manner
sorted_tuple = tuple(sorted(merged_tuple))
print("Sorted tuple:", sorted_tuple)
    # Step 6: Find the index of a particular fruit in the tuple
fruit_to_find = 'orange'
if fruit_to_find in sorted_tuple:
    index = sorted_tuple.index(fruit_to_find)
    print(f"The index of '{fruit_to_find}' in the sorted tuple is:", index)
else:
    print(f"'{fruit_to_find}' is not in the tuple.")
