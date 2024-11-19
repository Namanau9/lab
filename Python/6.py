#6.	Write a python program to create a dictionary of any five country-capital pairs. Perform the following tasks:
#i.	Add a new country-capital pair to the dictionary
#ii.	Change/Update the capital of one of the countries
#iii.	Delete a country-capital pair from the dictionary using the country name
#iv.	Print all the country-capitals in alphabetical order based on country name
#v.	Check if a particular country exists. If found display its capital name else display a message indicating that the country is not found

#creating a dictionary
country_capital = { "France": "Paris", "Japan": "Tokyo", "India" : "Mumbai", "Canada":"Ottawa"}
         #Adding a new pair
country_capital["Germany"] = "Berlin"
       #Update a capital of a country
country_capital["India"] = "New Delhi"
        #Deleting a pair
country_capital.pop("Japan")
         #Print all in alphabetical order based on country name
sorted_cc = dict( sorted( country_capital.items() ) )
print(" Country-Capital pair sorted by country name:", sorted_cc)
         #Check if a particular country exists
country_to_check = input("Enter the name of the country to check : ")
capital_found = None
for country, capital in country_capital.items():
            if country == country_to_check :
                    capital_found = capital
                    break

if  capital_found: 
          print( f"The capital of {country_to_check} is {capital_found}." )
else: 
         print(" The country {country_to_check} is not found in the dictionary.")
