#8.	Write a python program that takes as list of email addresses as a input from the user and filters out only a valid email addresses using regular expression. A valid email address must have the following format:
#i.	Starts with alphanumeric characters
#ii.	May contain periods(.), underscores ( _ ) , or dashes(-)
#iii.	Must contain exactly one @
#iv.	Should end with domain like .com, .org or .net


import re
def validate_emails(email_list):
            # Define a regular expression pattern for valid email addresses
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid_emails = []
        # Filter emails based on the pattern
    for email in email_list:
        if re.match(email_pattern, email.strip()):  # Use .strip() to remove extra spaces
            valid_emails.append(email.strip())
    return valid_emails

def extract_username_and_domain(valid_emails):
    email_details = []
       # Extract username and domain
    for email in valid_emails:
        username, domain = email.split('@')
        email_details.append((username, domain))
    return email_details
       # Accept a list of email addresses from the user
email_input = input("Enter a list of email addresses, separated by commas: ")
email_list = email_input.split(",")  # Split the input into a list
      # Validate emails
valid_emails = validate_emails(email_list)
print("Valid Emails:", valid_emails)

# Bonus: Extract username and domain
if valid_emails:
    email_info = extract_username_and_domain(valid_emails)
    for username, domain in email_info:
        print(f"Username: {username}, Domain: {domain}")
else:
    print("No valid emails were found.")
