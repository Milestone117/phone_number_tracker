def get_phone_number():
    while True:
        phone_number = input("Please enter your phone number with country code (e.g., +1 123-456-7890): ")
        
        # Remove any non-digit characters from the phone number
        phone_number = ''.join(char for char in phone_number if char.isdigit())
        
        # Check if the phone number is at least 11 digits long (including the country code)
        if len(phone_number) >= 11:
            return phone_number
        else:
            print("Invalid phone number. Please include the country code and try again.")

# Call the function to get the phone number
number = get_phone_number()
print(f"Your phone number is: {number}")