import csv
import datetime

def add_student():
  """Adds a new student record to the database."""
  first_name = input("Enter the student's first name: ")
  last_name = input("Enter the student's last name: ")
  dob = input("Enter the student's date of birth (YYYY-MM-DD): ")
  class_name = input("Enter the student's class name: ")
  section = input("Enter the student's section: ")
  unique_id = input("Enter the student's unique ID: ")
  address = input("Enter the student's address: ")

  with open("students.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([first_name, last_name, dob, class_name, section, unique_id, address])

def display_students():
  """Displays all the student records in the database."""
  with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
      print(row)  

def search_student():
  """Searches for a student record in the database."""
  unique_id = input("Enter the student's unique ID: ")

  with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
      if row[5] == unique_id:
        print(row)
        break
    else:
        print("Student not found.")

def modify_student():
    """Modifies a student record in the database."""
    unique_id = input("Enter the student's unique ID: ")

    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        students = list(reader)  # Convert the reader to a list

    found = False  # Flag to indicate if student was found
    modified_students = []
    
    for student in students:
      if len(student) >= 6 and student[5] == unique_id:
        found = True
        modified_student = []
        for field in student:
            new_value = input(f"Enter new value for '{field}': ")
            modified_student.append(new_value)
        modified_students.append(modified_student)
      else:
        modified_students.append(student)

    if found:
        with open("students.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(modified_students)
        print("Student record updated.")
    else:
        print("Student not found.")


def delete_student():
  """Deletes a student record from the database."""
  unique_id = input("Enter the student's unique ID: ")

  with open("students.csv", "r") as f:
    reader = csv.reader(f)
    students = []
    for row in reader:
      students.append(row)

  with open("students.csv", "w") as f:
    writer = csv.writer(f)
    for student in students:
      if student[5] != unique_id:
        writer.writerow(student)

  print("Student record deleted.")

def main():
  """The main function."""
  while True:
    print("Select an option:")
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Modify student")
    print("5. Delete student")
    print("6. Exit")

    option = input("Enter your option: ")

    if option == "1":
      add_student()
    elif option == "2":
      display_students()
    elif option == "3":
      search_student()
    elif option == "4":
      modify_student()
    elif option == "5":
      delete_student()
    elif option == "6":
      break
    else:
      print("Invalid option.")

if __name__ == "__main__":
  main()