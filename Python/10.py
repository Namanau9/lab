#10.	Write a python program that will create an excel file, store Name, Age, Place of n people as a data to it and read that data back. Accept the value of n from the user

import openpyxl
def main():
    file_name = 'people_data.xlsx'
     
    # Accept the number of entries from the user
    n = int(input("Enter the number of people: "))
    
    # Create a new workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Name'
    sheet['B1'] = 'Age'
    sheet['C1'] = 'Place'

    # Collect data and write it to the sheet
    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        place = input("Enter place: ")
        sheet.append([name, age, place])  # Append data as a new row

    # Save the workbook
    wb.save(file_name)
    print(f"Excel file '{file_name}' created.")

    # Read and print the data from the sheet
    print("Data in the Excel file:")
    for row in sheet.iter_rows(values_only=True):
        print(row)

if __name__ == "__main__":
    main()
