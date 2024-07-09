from flask import Flask
from student import Student, date 
import json
public_info = []
private_info = []
json_list = []


def main():
    
    register_search = input("Do you want to register or search for your child: ")
    if register_search.lower() == 'register':
        register()
    elif register_search.lower() == "search":
        search()
    else:
        print("Bad Output. Try Again")
        main()

def register():
    global public_info, private_info, json_list
    number = int(input("How many students do you wish to register: "))
    print()
    num = 1
    while num <= number:
        print(f"Student {num}")
        fname = input("Enter first name:\n")
        lname = input("Enter last name:\n")
        year = int(input("What year were they born in:\n"))
        month = int(input("What month were they born in(1-12):\n"))
        day = int(input("What day were they born in(1-31):\n"))
        gender = input("What gender are they:\n") 
        height = input("What is their height:\n")
        address = input("What is their address(House # + Street Name, City, State, Pin Code):\n")
        interest = input("What are their interests:\n")
        
        dob = date(year, month, day)
        t_year = date.today()
        age = t_year.year - dob.year

        if (t_year.month, t_year.day) < (dob.month, dob.day):
            age = (t_year.year - dob.year) - 1
        else:
            age = t_year.year - dob.year

        if age == 14:
            grade = 9
        elif age == 15:
            grade = 10
        elif age == 16:
            grade = 11
        elif age == 17:
            grade = 12
        else:
            print(["Student not Elgible"])
            main()
            break

        for i in public_info:
            if fname in i:
                if lname in i:
                    if age in i:
                        if interest in i:
                            print(f"Student {fname} {lname} already exists.")
                            break
            else:
                continue

        
        student = Student(fname, lname, grade, gender, height, address, interest)
        # reg_obj = {"fname": fname, "lname": lname, "age": age, "gender": gender, "height": height, "address": address, "interest": interest}
        # student_obj = {"fname": fname, "lname": lname, "grade": grade, "Interest": interest}

        student_str = json.dumps(student.to_json())

        print(student_str)

        
        json_dict = student.__dict__
        with open("data.json") as jsonfile:
            json_list = json.load(jsonfile)
    
        json_list.append(json_dict)

        with open("data.json", "w") as jsonfile:
            json.dump(json_list, jsonfile, indent=4, separators=(",", ": "))

        private_info.append(student.getPrivate())
        public_info.append(student.getPublic())

        
        num += 1

def search():

    search_req = input("Do you wish to see the public or private profile of your student: ")
    if search_req.lower() == "public":
        fname_search = input("Enter first name of desired student: ")
        lname_search = input("Enter last name of desired student: ")
        grade_search = int(input("Enter current grade of student: "))
        interest_search = input("Enter interest(s) that student is pursuing: ")
        with open("data.json", "r") as jsonfile:
            load = json.load(jsonfile)
            for i in load:
                if i.get("fname") == fname_search:
                    if i.get("lname") == lname_search:
                        if i.get("grade") == grade_search:
                            if i.get("interest") == interest_search:
                                print(f"We have discovered student {fname_search} {lname_search} within our databse.")
                                student = Student(fname_search, lname_search, grade_search, None, None, None, interest_search)
                                print("Public Information is below:")
                                print()
                                print(student.getPublic())
                            else:
                                print("Student could not be located.")
                                go_back = input("Do you wish to return to the register page(yes/no): ")
                                if go_back.lower() == "yes":
                                    register()
                                elif go_back.lower() == "no":
                                    print("You may contact this number for further enquieres. Contact info: (925)-334-9095")
                                    print("Good day.")
                                else:
                                    print("Wrong input. Good Day.")
    elif search_req.lower() == "private":
        num = 1

        while num < 5:
            password = int(input("Enter passowrd: "))
            if password == 123456:
                fname_search = input("Enter first name of desired student: ")
                lname_search = input("Enter last name of desired student: ")
                grade_search = int(input("Enter current grade of student: "))
                interest_search = input("Enter interest(s) of student: ")
                with open("data.json", "r") as jsonfile:
                    load = json.load(jsonfile)
                    for i in load:
                        if i.get("fname") == fname_search:
                            if i.get("lname") == lname_search:
                                if i.get("grade") == grade_search:
                                    if i.get("interest") == interest_search:
                                        bool = True
                                        print(f"\nWe have loacted the private information of student {fname_search} {lname_search} within our database.")
                                        student = Student(fname_search, lname_search, grade_search, i.get("gender"), i.get("height"), i.get("_address"), interest_search)
                                        print("\nPrivate Information of Student is below:\n")
                                        print(student.getPrivate()+"\n")
                                    else:
                                        bool = False
                                        print("We could not locate student {} {} in our student.".format(fname_search, lname_search))
            
            else:
                print("Wrong Passoword.")
                password = int(input("Enter passowrd: "))
            if num == 5:
                print("You have been locked out of the system for too many poor tries. Good day.")
 
            
            if bool == True:
                break
            else:
                continue
