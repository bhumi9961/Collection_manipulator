📘 Student Data Organizer
📌 Project Overview
The Student Data Organizer is a Python-based console application designed to manage student records efficiently. It demonstrates the use of core Python concepts such as string formatting, data structures (List, Tuple, Set, Dictionary), mutability, immutability, type casting, and the del keyword.

🎯 Objectives
Store and manage student data
Demonstrate Python collection data types
Apply string formatting techniques
Understand mutable vs immutable data
Perform operations like add, update, delete, and display

⚙️ Features
✅ 1. Add Student
Input student details:
ID
Name
Age
Grade
Date of Birth
Subjects
Stores:
Immutable data (ID & DOB) using Tuple
Other details using Dictionary
Adds records to:
List (for storage)
Dictionary (for fast lookup)
📋 2. Display All Students
Displays all student records in a formatted way
Uses:
f-strings
.join() for subject display
✏️ 3. Update Student Information
Update:
Name
Age
Grade
Demonstrates mutability of Dictionary

❌ 4. Delete Student
Deletes student using student ID
Uses:
del keyword on list and dictionary

📚 5. Display Unique Subjects
Shows all unique subjects offered
Uses Set to avoid duplicates

🚪 6. Exit
Safely exits the program

🧠 Concepts Used
🔹 1. List (Mutable)
Stores multiple student records:
student_list.append(student)
🔹 2. Tuple (Immutable)
Stores fixed student data:
personal_info = (student_id, birthday)
🔹 3. Set (Unique Values)
Stores unique subjects:
subject_set.update(subject)
🔹 4. Dictionary
Maps student ID to student data:
student_dict[student_id] = student
🔹 5. String Formatting
f-strings → f"Student {name} added"
.join() → for subjects display
🔹 6. Type Casting
int(input("Enter ID: "))
🔹 7. del Keyword
del student_list[i]
del student_dict[sid]

▶️ How to Run
Make sure Python is installed
Save the file as:
student_data_organizer.py
Run the program:
python student_data_organizer.py

📌 Example Menu
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Student Offered
6. Exit

🏁 Conclusion
This project provides hands-on experience with Python fundamentals and demonstrates how different data structures work together to build a practical application.
