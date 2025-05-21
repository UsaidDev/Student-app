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
    details=student_detail()
    if details:
       student,age,location=details
       Near_By=nearby_school()

       if Near_By == "1":# 1=1
           Sub=subject_selection()
           if Sub == "1":
               data=[{
               "Name":student,
               "Age":age,
               "Location":location,
               "School":"Loyola School",
               "Subject":"Science"
           }]
               showindex = range(1, len(data)+1)
               print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=showindex))
           else:
                print("Subject not selected.")
       else:
           print("Not near a school")    
    else:
        print("Invalid details.")


def nearby_school():
    print("Please select nearby school")
    print("1:-Loyola School")
    print("2:-Kendriya Vidyalaya school")
    print("3:-Arya Central School")
    choise=input('Please select the school number:')
    return choise

def subject_selection():
    print("Please Select the Subject:")
    print("1:Science")
    print("2:Commerce")
    print("3:Humanities")
    subject=input("Please select the subject number:")
    return subject

process_data()