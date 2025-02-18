#a function to add students to our attendance list
def add_student(students, name):
    students[name] = False
    print(f"student {name} has been added successfully")

#a function to mark students  attendance 
def mark_attendance(students, name):
    if name in students:
     students[name] = True
     print(f"student {name} attendance has been recorded successfully") 

    else:
       print(f"student {name} has not been found") 

# function to display attendace of the students
def display_attendance(students):
   print("\nThis is the scitt attendance record: ")
   for name, is_present in students.items():
      status = "present" if is_present else "absent" 
      print(f"{name}:{status}")

# main 
def main():
   students = {}

   while True:
      print("\nWelcome to scitt attendance system")
      print("1. add student name")
      print("2. mark attendance list")
      print("3. display attendance")
      print("4. exit")

      selection = input("enter your selection choice(1-4)")

      if selection == "1":
         name = input("enter student name:  ")
         add_student(students, name)

      elif selection == "2":
         name = input("enter student name:  ")
         mark_attendance(students, name)

      elif selection == "3":
         display_attendance(students)

      elif selection == "4":
         print("thank you for using scitt attendance system developed by IT fusion")

      else:
         print("invalid choice! please enter a valid choice between (1-4)")

if __name__ == "__main__":
   main()
         




