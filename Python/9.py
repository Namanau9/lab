#9.	Write a python program that create a text file write some lines into it, read the contents from the fille and then display it

def write_to_file(file_name):
    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Write some lines to the file
        file.write("Hello, World!\n")
        file.write("This is a simple file handling example.\n")
        file.write("Python is great for file operations.\n")

def read_from_file(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the content of the file
        content = file.read()
        return content

# Main program
file_name = 'example.txt'

# Write to file
write_to_file(file_name)
print(f"Data written to {file_name}")

# Read from file
file_content = read_from_file(file_name)
print("Content of the file:")
print(file_content)
