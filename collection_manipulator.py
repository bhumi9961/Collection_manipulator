print("Welcome to the Student Data Organizer")

student_dict = {}
student_list = []
subject_set = set()

while True:
    print("Select an option:\n" \
    "1. Add Student\n" \
    "2. Display All Students\n" \
    "3. Update Student Information\n" \
    "4. Delete Student\n" \
    "5. Display Student Offered\n" \
    "6. Exit")

    choice = int(input("Enter Your Choice: "))   

    if choice == 1:
        print("Enter student Details:")
        student_id = int(input("Enter Student ID: "))
        name = str(input("Enter Name: "))
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        birthday = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")
        subject = {s.strip() for s in subjects.split(",")}
        personal_info = (student_id, birthday)
        student = {
            "Personal" : personal_info,
            "Name" : name,
            "Age": age,
            "Grade" : grade,
            "Subjects" : subject_set
        }
        student_list.append(student)
        student_dict[student_id] = student
        subject_set.update(subject)

        print(f"Student {name} added successfully!!")
        
    elif choice == 2:
        print("\n --------- Display Student records ---------")

        if not student_list:
            print("No student record found!!")
        else: 
            for s in student_list:
                print(f"\nID: {personal_info[0]} | Name: {name} | Age: {age} | Grade: {grade}")
                print(f"DOB: {personal_info[1]}")
                print("Subjects:", ", ".join(s["Subjects"]))

    elif choice == 3:
        sid = int(input("Enter Student ID to update: "))

        if sid in student_dict:
            print("1. Update Name\n2. Update Age\n3. Update Grade")
            ch = int(input("Enter choice: "))

            if ch == 1:
                student_dict[sid]["Name"] = input("New Name: ")
            elif ch == 2:
                student_dict[sid]["Age"] = int(input("New Age: "))
            elif ch == 3:
                student_dict[sid]["Grade"] = input("New Grade: ")

            print("Student updated successfully!")

        else:
            print("Student not found!")

    elif choice == 4:
        sid = int(input("Enter Student ID to delete: "))

        if sid in student_dict:
            for i in range(len(student_list)):
                if student_list[i]["Personal"][0] == sid:
                    del student_list[i]   
                    break
            del student_dict[sid]        
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    
    elif choice == 5:
        print("\nUnique Subjects Offered:")
        print(", ".join(subject_set))

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
