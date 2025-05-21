from tabulate import tabulate

def student_detail():

    student=input("Enter your name🎉:")
    if not student.strip().replace(" ", "").isalpha():
        print("❌ Name should have only letters")
        student=input("Enter your name again❗️: ")
        if not student.strip().isalpha():
            print("❌ Invalid again, stopping now⚠️")
            return None
        
    age=input(str("Age 👍:"))
    if not age.isdigit():
        print("❌ Age should be a number")
        age=input(str("Enter your Age Again🔄:"))
        if not age.isdigit():
            print("Invalid again, stopping now🚫")
            return None
        
    location=input("Location📍:")
    if not location.strip().replace(" ", "").isalpha():
        print("❌ Location should have only letters")
        location=input("Enter your location again⏳:")
        if not location.strip():
            print("Invalid again, stopping now❗️")
            return None
    return student,age,location

def process_data(): # Do next task's
    total_details=int(input("How many students do you want to enter? "))
    all_data= [] #Store all student info

    for _ in range(total_details):
        details=student_detail()
        if details:
            student, age, location =details
            school = nearby_school()
            if not school:
                print("Invalid school selection")
                continue
            subject=subject_selection()
            if not subject:
                print("Invalid selection")
                continue

            entry={
                "Name":student,
                "Age":age,
                "Loaction":location,
                "School":school,
                "Subject":subject
            }
            all_data.append(entry)
        else:
            print("Invaild details")

    if all_data:
        print(tabulate(all_data, headers='keys', tablefmt='fancy_grid',showindex = range(1, len(all_data)+1)))
    else:
        print("No valid student data entered.")

def nearby_school():
    print("Please select nearby school")
    print("1:-Loyola School")
    print("2:-Kendriya Vidyalaya school")
    print("3:-Arya Central School")
    choise=input('Please select the school number:')

    if choise == "1":
        return "Loyola School"
    if choise == "2":
        return "Kendriya School"
    if choise == "3":
        return "Arya Central School"
    return choise

def subject_selection():
    print("Please Select the Subject:")
    print("1:Science")
    print("2:Commerce")
    print("3:Humanities")
    subject=input("Please select the subject number:")

    if subject == "1":
        return "Science"
    if subject == "2":
        return "Commerce"
    if subject == "3":
        return "Humanities"
    return subject

if __name__ == "__main__":
    process_data()