# 1. Collect Dynamic Employee Inputs
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = first_name + ' ' + last_name

address = input("Enter primary address (e.g., Lions Gate Apartment): ")
address_unit = input("Enter unit/apartment number (e.g., Apartment D4): ")
address += ', ' + address_unit

# Using try-except blocks to safely handle number conversions
try:
    employee_age = int(input("Enter employee age: "))
except ValueError:
    print("Invalid age entered. Defaulting to 0.")
    employee_age = 0

try:
    experience_years = int(input("Enter years of experience: "))
except ValueError:
    print("Invalid experience entered. Defaulting to 0.")
    experience_years = 0

position = input("Enter job position: ")

try:
    salary = float(input("Enter salary ($): "))
except ValueError:
    print("Invalid salary entered. Defaulting to 0.00.")
    salary = 0.00

employee_code = input("Enter employee code (e.g., DEV-2026-JD-001): ")

# 2. Process and Format the Data
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
experience_info = 'experience: ' + str(experience_years) + ' years'
employee_card = f'employee: {full_name} | Age: {employee_age} | Position: {position} | Salary ${salary:,.2f}'

# String slicing based on your code structure
department = employee_code[0:3]
initials = employee_code[9:11]
details = department + ' ' + initials

# 3. Display the Clean Output
print("\n--- Employee Profile Generated ---")
print(details, employee_card, experience_info, sep='\n')
