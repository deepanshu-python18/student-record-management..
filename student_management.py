print("===== STUDENT RECORD MANAGEMENT SYSTEM =====")

print("1. Add Student")
print("2. View All Students")
print("3. Search Student")
print("4. Calculate Average Marks")
print("5. Exit")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    print("Add Student selected!")

elif choice == "2":
    print("View All Students selected!")

elif choice == "3":
    print("Search Student selected!")

elif choice == "4":
    print("Calculate Average Marks selected!")

elif choice == "5":
    print("Thank you for using our system!")

else:
    print("Invalid choice! Please try again.")
    
if choice == "1":
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    print("\nStudent Added Successfully!")
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    with open("students.txt", "a") as file:
         file.write(name + "," + str(age) + "," + str(marks) + "\n")
elif choice == "2":
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        if len(records) == 0:
            print("No student records found!")

        else:
            for record in records:
                name, age, marks = record.strip().split(",")
                print(name, age, marks)

    except FileNotFoundError:
        print("No student records found!")
elif choice == "3":
    search_name = input("Enter student name to search: ")

    found = False

    with open("students.txt", "r") as file:
        for record in file:
            name, age, marks = record.strip().split(",")

            if name.lower() == search_name.lower():
                print("\nStudent Found!")
                print("Name:", name)
                print("Age:", age)
                print("Marks:", marks)
                found = True
                break

    if not found:
        print("Student not found!")
elif choice == "4":
    total = 0
    count = 0

    with open("students.txt", "r") as file:
        for record in file:
            name, age, marks = record.strip().split(",")

            total += float(marks)
            count += 1

    if count > 0:
        average = total / count
        print("Average Marks:", average)
    else:
        print("No student records found!")
def search_student():
    while True:
        search_name = input(
            "\nEnter student name (or type 'back' to return): "
        )

