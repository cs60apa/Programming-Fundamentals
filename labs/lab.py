import datetime

name = input("Enter your name: ")
birth_year_input = input("Enter your birth year: ")

try:
    birth_year = int(birth_year_input)
    current_year = datetime.date.today().year
    
    age = current_year - birth_year
    
    print(f"Hello {name}! Since it's {current_year}, you are {age} years old.")

except ValueError:
    print("Oops! Please enter a valid number for the birth year.")