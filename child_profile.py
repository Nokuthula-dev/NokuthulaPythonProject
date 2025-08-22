# --------------------------------------------
# Child Profile Program (variables + constants)
# --------------------------------------------
# Demonstrates variables, constants, and the print() function

# CONSTANT (written in UPPERCASE)
SCHOOL_NAME = "Dominican Convent Primary"   # Constant value: does not change

# VARIABLES (can change if needed)
child_name = "Nalenhle"    # Name of the child
child_age = 8              # Age of the child
child_gender = "Girl"      # Gender of the child
child_grade = "3M"         # Class/Grade of the child
hobbies = ["Swimming"]     # List of hobbies

# PRINTING OUTPUT (using the print() function to display details)
print("Child Profile")
print("-------------")
print("Name:", child_name)
print("Gender:", child_gender)
print("Age:", child_age, "years old")
print("Grade:", child_grade)
print("School:", SCHOOL_NAME)
print("Hobbies:", ", ".join(hobbies))  # Join list items into a string

# SUMMARY SENTENCE (shows how variables are used in text)
print("\nSummary:")  # \n adds a blank line
print(f"{child_name} is an {child_age}-year-old {child_gender} in Grade {child_grade} at {SCHOOL_NAME}.")

# CALCULATING AGE NEXT YEAR (shows how variables can change)
child_age_next_year = child_age + 1
print(f"Next year, {child_name} will be {child_age_next_year} years old.")
