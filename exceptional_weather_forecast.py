'''
Objective: The aim of this assignment is to enhance your understanding of exception 
handling by creating a weather forecast application that gracefully handles 
unexpected user input and provides user-friendly error messages.
'''

# Task 1: Start 
# Begin by asking the user to enter the temperature in Fahrenheit.

# temperature_in_fahrenheit = int(input("Please enter temperature in Fahrenheit: "))

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit 
# temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
try:
    while True:
        try:
            temp_fahrenheit = float(input("Please enter temperature in Fahrenheit: "))
            temp_celcius = (temp_fahrenheit - 32) * 5/9
        
        except ValueError:
            print("Please enter a numeric value.")
            continue
        else:
            print (f"The temperature in Celcius is {temp_celcius :.1f}\u00B0C")
    
        user_input = input("Would you like to enter another number? (yes/no) ").lower()
        if user_input != "yes":
            break
finally:
    print("Thank you for using the weather forecast application.")

# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?

# Task 3: User Experience Implement an else block that prints the converted 
# temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

#Task 4: Finally Add a finally block that thanks the user for using the weather 
# forecast application, ensuring that this message is displayed regardless of 
# whether an exception was caught or not.