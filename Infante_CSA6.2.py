
import re

student_id = input("Enter your student ID: ")
pattern = r"\d{4}-\d{4}"
if re.match(pattern, student_id):
    print("Valid Student ID.")
else:
    print("Invalid Student ID.")